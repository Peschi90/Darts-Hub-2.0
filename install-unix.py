#!/usr/bin/env python3
"""User-level installer for Linux/macOS. No modules start during installation."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import plistlib
import re
import shutil
import shlex
import sys
import struct
import subprocess
import tarfile
import tempfile
import urllib.request

REPO = 'Peschi90/Darts-Hub-2.0'
SEMVER = re.compile(r'^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$')

LOGO = r'''       _____    _    _                    __/|
      |  __ \  | |  | |                  /_/_/
      | |  | | | |__| |                    /
      | |  | | |  __  |                   /
      | |__| | | |  | |          ________/
      |_____/  |_|  |_|         /'''


def styled(text, color='36'):
    use_color = sys.stdout.isatty() and 'NO_COLOR' not in os.environ and os.environ.get('TERM') != 'dumb'
    print('\033[' + color + 'm' + text + '\033[0m' if use_color else text)


def show_header(rid):
    print()
    styled(LOGO)
    styled('  DARTS-HUB 2.0  |  ONLINE INSTALLER', '97')
    styled('  --------------------------------------------------------', '36')
    styled('  System: ' + rid + '    |    get.darts-hub.de')
    styled('  GUI / TUI / HEADLESS  -  Dein Setup. Dein Spiel.', '90')
    print()


def show_step(number, title):
    print()
    styled('  [%d/3] %s' % (number, title))
    styled('  --------------------------------------------------------')


def version_key(tag):
    match = SEMVER.fullmatch(tag)
    if not match:
        raise ValueError('Invalid release version: ' + tag)
    suffix = match[4]
    identifiers = tuple((0, int(v)) if v.isdigit() else (1, v) for v in suffix.split('.')) if suffix else ()
    return tuple(int(match[i]) for i in (1, 2, 3)), suffix is None, identifiers


def runtime(system, machine, bits=64):
    if bits != 64:
        raise ValueError("32-bit OS/userspace is not supported by the published packages. Use 64-bit Raspberry Pi OS for linux-arm64.")
    os_name = {'Linux': 'linux', 'Darwin': 'osx'}.get(system)
    arch = {'x86_64': 'x64', 'amd64': 'x64', 'aarch64': 'arm64', 'arm64': 'arm64'}.get(machine.lower())
    if not os_name or not arch:
        raise ValueError('Supported: Linux/macOS, x64/ARM64. Detected: ' + system + '/' + machine)
    return os_name + '-' + arch


def detect_runtime():
    system, machine = platform.system(), platform.machine()
    bits = struct.calcsize('P') * 8
    if system == 'Linux' and shutil.which('getconf'):
        result = subprocess.run(['getconf', 'LONG_BIT'], capture_output=True, text=True, check=True, timeout=5)
        bits = int(result.stdout.strip())
    if system == 'Darwin':
        result = subprocess.run(['/usr/sbin/sysctl', '-n', 'hw.optional.arm64'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip() == '1':
            machine = 'arm64'
    return runtime(system, machine, bits)


def choose_release(releases, beta, rid):
    name = 'dartshub-' + rid + '.tar.gz'
    candidates = [r for r in releases if not r.get('draft') and (beta or not r.get('prerelease')) and SEMVER.fullmatch(r.get('tag_name', ''))]
    if not candidates:
        raise ValueError('No matching published release found.')
    release = max(candidates, key=lambda r: version_key(r['tag_name']))
    asset = next((a for a in release['assets'] if a['name'] == name), None)
    if asset is None:
        raise ValueError('Latest release is missing ' + name + '. Try again after release publishing completes.')
    return release, asset


def download_asset(asset, destination):
    url = asset['browser_download_url']
    if not url.startswith('https://github.com/' + REPO + '/releases/download/'):
        raise ValueError('Unexpected release download URL.')
    digest = asset.get('digest', '')
    if not re.fullmatch(r'sha256:[0-9a-fA-F]{64}', digest):
        raise ValueError('Release has no SHA256 digest. Use a newly uploaded release.')
    request = urllib.request.Request(url, headers={'User-Agent': 'DartsHub-Installer'})
    sha = hashlib.sha256()
    total = 0
    with urllib.request.urlopen(request, timeout=60) as source, open(destination, 'wb') as output:
        while True:
            block = source.read(1024 * 1024)
            if not block:
                break
            total += len(block)
            if total > 1024 ** 3:
                raise ValueError('Archive exceeds 1 GB.')
            sha.update(block)
            output.write(block)
            print('\rDownload: %d MB' % (total // 1024 ** 2), end='', flush=True)
    print()
    if sha.hexdigest().lower() != digest[7:].lower():
        raise ValueError('SHA256 mismatch. Installation canceled.')


def extract_archive(archive, destination):
    with tarfile.open(archive, 'r:gz') as bundle:
        entries = bundle.getmembers()
        if sum(max(e.size, 0) for e in entries) > 2 * 1024 ** 3 or len(entries) > 10000:
            raise ValueError('Expanded archive is too large.')
        for entry in entries:
            path = PurePosixPath(entry.name)
            if path.is_absolute() or '..' in path.parts or '\\' in entry.name or not (entry.isfile() or entry.isdir()):
                raise ValueError('Unsafe archive entry: ' + entry.name)
        # All links and special entries have already been rejected (also on older Python).
        if hasattr(tarfile, 'data_filter'):
            bundle.extractall(destination, members=entries, filter='data')
        else:
            bundle.extractall(destination, members=entries)


def quote_systemd(value):
    return '"' + str(value).replace('\\', '\\\\').replace('"', '\\"').replace('%', '%%').replace('\n', '\\n') + '"'


def register_autostart(executable, mode, minimized, config_home, home, system, run=subprocess.run):
    target = 'gui' if mode == 'gui' else 'headless'
    args = ['--headless', '--background'] if target == 'headless' else ['--minimized'] if minimized else []
    if system == 'Linux':
        if target == 'headless':
            path = config_home / 'systemd/user/dartshub.service'
            text = '[Unit]\nDescription=DartsHub headless\nAfter=network-online.target\n\n[Service]\nType=simple\nExecStart=' + ' '.join(map(quote_systemd, [str(executable)] + args)) + '\nRestart=on-failure\nRestartSec=3\nTimeoutStopSec=20\n\n[Install]\nWantedBy=default.target\n'
        else:
            path = config_home / 'autostart/dartshub.desktop'
            quoted = '"' + str(executable).replace('\\', '\\\\').replace('"', '\\"').replace('`', '\\`').replace('$', '\\$').replace('%', '%%') + '"'
            text = '[Desktop Entry]\nType=Application\nName=DartsHub\nExec=' + quoted + (' --minimized' if minimized else '') + '\nTerminal=false\nX-GNOME-Autostart-enabled=true\n'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        if target == 'headless':
            run(['systemctl', '--user', 'daemon-reload'], check=True)
            run(['systemctl', '--user', 'enable', 'dartshub.service'], check=True)
            print('User service starts at login. For boot without login: sudo loginctl enable-linger ' + os.environ.get('USER', '<user>'))
    else:
        path = home / ('Library/LaunchAgents/de.darts-hub.' + target + '.plist')
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {'Label': 'de.darts-hub.' + target, 'ProgramArguments': [str(executable)] + args, 'RunAtLoad': True}
        if target == 'headless':
            data['KeepAlive'] = {'SuccessfulExit': False}
        path.write_bytes(plistlib.dumps(data))
        # Register at next login. Immediate launch is handled separately, avoiding duplicate processes.
    return path


def ask(prompt, default):
    value = input(prompt + ' [' + default + ']: ').strip()
    return value or default


def create_desktop_shortcut(executable, mode, desktop, system):
    desktop.mkdir(parents=True, exist_ok=True)
    if system == 'Darwin' and mode == 'gui':
        link = desktop / 'DartsHub.app'
        bundle = executable.parents[2]
        if link.is_symlink() and link.resolve() == bundle.resolve():
            return link
        link.symlink_to(bundle, target_is_directory=True)
    elif system == 'Darwin':
        link = desktop / 'DartsHub-TUI.command'
        link.write_text('#!/bin/sh\nexec ' + shlex.quote(str(executable)) + ' --tui\n', encoding='utf-8')
        link.chmod(0o755)
    else:
        link = desktop / ('DartsHub-' + mode + '.desktop')
        quoted = '"' + str(executable).replace('\\', '\\\\').replace('"', '\\"').replace('`', '\\`').replace('$', '\\$').replace('%', '%%') + '"'
        link.write_text('[Desktop Entry]\nType=Application\nName=DartsHub ' + mode.upper() + '\nExec=' + quoted + (' --tui' if mode == 'tui' else '') + '\nTerminal=' + ('true' if mode == 'tui' else 'false') + '\n', encoding='utf-8')
        link.chmod(0o755)
    return link


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--channel', choices=['stable', 'beta'])
    parser.add_argument('--mode', choices=['gui', 'tui', 'headless'])
    parser.add_argument('--directory')
    parser.add_argument('--no-start', action='store_true')
    options = parser.parse_args()
    if os.geteuid() == 0:
        raise ValueError('Run as your normal user, without sudo.')
    rid = detect_runtime()
    show_header(rid)
    show_step(1, 'Setup / Einrichtung')
    channel = options.channel or ask('Channel / Kanal: stable, beta', 'stable').lower()
    mode = options.mode or ask('Mode / Betriebsart: gui, tui, headless', 'gui').lower()
    if channel not in ('stable', 'beta') or mode not in ('gui', 'tui', 'headless'):
        raise ValueError('Invalid channel or mode.')
    home = Path.home()
    default = home / ('Applications/DartsHub' if rid.startswith('osx') else '.local/share/dartshub-app')
    target = Path(options.directory or ask('Install directory / Installationsordner', str(default))).expanduser().absolute()
    if '\n' in str(target) or '\r' in str(target) or target == home or target == Path('/'):
        raise ValueError('Choose a dedicated application directory.')
    autostart = ask('Autostart at login / Bei Anmeldung starten? yes/no', 'no').lower() in ('yes', 'y', 'ja', 'j')
    minimized = mode == 'gui' and autostart and ask('Start minimized / Minimiert starten? yes/no', 'no').lower() in ('yes', 'y', 'ja', 'j')
    desktop_shortcut = mode in ('gui', 'tui') and ask('Create desktop shortcut / Desktop-Verknuepfung erstellen? yes/no', 'yes').lower() in ('yes', 'y', 'ja', 'j')
    if mode == 'tui' and autostart:
        print('TUI autostart runs the headless backend; open --tui when you want to configure it.')
    request = urllib.request.Request('https://api.github.com/repos/' + REPO + '/releases?per_page=100', headers={'User-Agent': 'DartsHub-Installer', 'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        release, asset = choose_release(json.load(response), channel == 'beta', rid)
    show_step(2, 'Download & Installation')
    if rid.startswith('linux') and not any(shutil.which(player) for player in ('ffplay', 'paplay', 'aplay')):
        print('No Caller audio player found. For WAV/MP3: sudo apt install ffmpeg; for WAV: pulseaudio-utils or alsa-utils')
    print('Installing ' + release['tag_name'] + ' -> ' + str(target))
    if target.exists() and ask('Existing directory. Close DartsHub first. Continue? yes/no', 'no').lower() not in ('yes', 'y', 'ja', 'j'):
        return
    if any(p.is_symlink() for p in [target] + list(target.parents)):
        raise ValueError('Installation path must not contain symbolic links.')
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='dartshub-install-', dir=target.parent) as work:
        staging = Path(work) / 'app'
        staging.mkdir()
        archive = Path(work) / 'release.tar.gz'
        download_asset(asset, archive)
        extract_archive(archive, staging)
        relative = Path('DartsHub.app/Contents/MacOS/DartsHub') if rid.startswith('osx') else Path('DartsHub')
        if not (staging / relative).is_file():
            raise ValueError('Archive does not contain DartsHub.')
        for path in staging.rglob('*'):
            current = target / path.relative_to(staging)
            if current.is_symlink() or any(p.is_symlink() for p in current.parents):
                raise ValueError('Existing installation contains symbolic links.')
        # Merge only shipped files. Settings/logs and other local files are preserved.
        # Keep locally saved event libraries, but seed missing files from this release.
        def preserve_libraries(source, names):
            folder = Path(source)
            if folder.name != 'event-templates':
                return []
            return [name for name in names if (target / folder.relative_to(staging) / name).exists()]
        shutil.copytree(staging, target, dirs_exist_ok=True, ignore=preserve_libraries)
    executable = target / relative
    executable.chmod(executable.stat().st_mode | 0o111)
    if desktop_shortcut:
        desktop = home / 'Desktop'
        if platform.system() == 'Linux' and shutil.which('xdg-user-dir'):
            result = subprocess.run(['xdg-user-dir', 'DESKTOP'], capture_output=True, text=True, check=True)
            if result.stdout.strip():
                desktop = Path(result.stdout.strip())
        create_desktop_shortcut(executable, mode, desktop, platform.system())
    # GUI desktop launcher is also usable without autostart.
    if autostart:
        config_home = Path(os.environ.get('XDG_CONFIG_HOME', str(home / '.config')))
        if not config_home.is_absolute():
            config_home = home / '.config'
        register_autostart(executable, mode, minimized, config_home, home, platform.system())
    show_step(3, 'Ready / Fertig')
    styled('  DartsHub ist bereit / DartsHub is ready.', '32')
    print('  Version: ' + release['tag_name'])
    print('  Mode:    ' + mode.upper())
    print('  Folder:  ' + str(target))
    print('  Autostart: %s    Desktop shortcut: %s' % (autostart, desktop_shortcut))
    print('\nStart: ' + str(executable) + (' --' + mode if mode != 'gui' else ''))
    if rid.startswith('osx'):
        print('If macOS blocks an unsigned application, allow it in System Settings > Privacy & Security.')
    if not options.no_start and ask('Start now / Jetzt starten? yes/no', 'yes').lower() in ('yes', 'y', 'ja', 'j'):
        if mode == 'tui':
            subprocess.run([str(executable), '--tui'], cwd=target, check=True)
        elif autostart and mode == 'headless' and platform.system() == 'Linux':
            subprocess.run(['systemctl', '--user', 'start', 'dartshub.service'], check=True)
        else:
            args = ['--headless', '--background'] if mode == 'headless' else ['--minimized'] if minimized else []
            with open(os.devnull, 'wb') as output:
                subprocess.Popen([str(executable)] + args, cwd=target, stdin=subprocess.DEVNULL, stdout=output, stderr=output, start_new_session=True)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit('Installation failed / fehlgeschlagen: ' + str(error))
