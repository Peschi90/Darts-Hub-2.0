#!/bin/sh
set -eu
command -v curl >/dev/null || { echo 'curl is required.' >&2; exit 1; }
command -v python3 >/dev/null || { echo 'Python 3 is required. Install python3 and run this installer again.' >&2; exit 1; }
work=$(mktemp -d)
trap 'rm -f "$work/install-unix.py"; rmdir "$work"' EXIT HUP INT TERM
curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 \
  https://get.darts-hub.de/install-unix.py -o "$work/install-unix.py"
# Prompts must read the terminal, even when the bootstrap was piped into sh.
python3 "$work/install-unix.py" "$@" </dev/tty
