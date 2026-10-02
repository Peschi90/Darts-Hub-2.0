#requires -Version 5.1
param(
    [ValidateSet('stable', 'beta')][string]$Channel,
    [ValidateSet('gui', 'tui', 'headless')][string]$Mode,
    [string]$Directory,
    [switch]$NoStart
)
$ErrorActionPreference = 'Stop'
$Repository = 'Peschi90/Darts-Hub-2.0'

function Read-Choice([string]$Prompt, [string]$Default) {
    $answer = Read-Host "$Prompt [$Default]"
    if ([string]::IsNullOrWhiteSpace($answer)) { return $Default }
    return $answer.Trim().ToLowerInvariant()
}
function Test-Yes([string]$Answer) { return $Answer -in @('yes', 'y', 'ja', 'j') }
function Get-ReleaseVersion([string]$Tag) {
    if ($Tag -notmatch '^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$') { throw "Invalid version: $Tag" }
    return [version]"$($Matches[1]).$($Matches[2]).$($Matches[3])"
}
function Compare-ReleaseTags([string]$Left, [string]$Right) {
    Add-Type -AssemblyName System.Numerics
    $comparison = (Get-ReleaseVersion $Left).CompareTo((Get-ReleaseVersion $Right))
    if ($comparison -ne 0) { return $comparison }
    $leftParts = (($Left -split '\+', 2)[0] -split '-', 2)
    $rightParts = (($Right -split '\+', 2)[0] -split '-', 2)
    if ($leftParts.Count -eq 1) { if ($rightParts.Count -eq 1) { return 0 }; return 1 }
    if ($rightParts.Count -eq 1) { return -1 }
    $a = $leftParts[1].Split('.'); $b = $rightParts[1].Split('.')
    for ($i = 0; $i -lt [Math]::Min($a.Count, $b.Count); $i++) {
        $an = $a[$i] -match '^[0-9]+$'; $bn = $b[$i] -match '^[0-9]+$'
        if ($an -and $bn) { $comparison = ([System.Numerics.BigInteger]::Parse($a[$i])).CompareTo([System.Numerics.BigInteger]::Parse($b[$i])) }
        elseif ($an -ne $bn) { if ($an) { $comparison = -1 } else { $comparison = 1 } }
        else { $comparison = [string]::CompareOrdinal($a[$i], $b[$i]) }
        if ($comparison -ne 0) { return $comparison }
    }
    return $a.Count.CompareTo($b.Count)
}
function Select-Release($Releases, [bool]$Beta, [string]$Rid) {
    $best = $null
    foreach ($release in $Releases) {
        if ($release.draft -or (-not $Beta -and $release.prerelease)) { continue }
        try { $null = Get-ReleaseVersion $release.tag_name } catch { continue }
        if ($null -eq $best -or (Compare-ReleaseTags $release.tag_name $best.tag_name) -gt 0) { $best = $release }
    }
    if ($null -eq $best) { throw 'No matching published release found.' }
    $asset = @($best.assets | Where-Object name -EQ "dartshub-$Rid.zip")
    if ($asset.Count -ne 1) { throw "Latest release is missing dartshub-$Rid.zip. Try again after publishing completes." }
    return @{ Release = $best; Asset = $asset[0] }
}
function Expand-SafeRelease([string]$Archive, [string]$Destination) {
    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead($Archive)
    try {
        $expanded = 0L
        $root = [System.IO.Path]::GetFullPath($Destination) + [System.IO.Path]::DirectorySeparatorChar
        if ($zip.Entries.Count -gt 10000) { throw 'Too many archive entries.' }
        foreach ($entry in $zip.Entries) {
            $name = $entry.FullName.Replace('\', '/')
            $expanded += $entry.Length
            if ($expanded -gt 2GB -or $name.StartsWith('/') -or $name.Contains(':') -or ($name.Split('/') -contains '..')) { throw 'Unsafe release archive.' }
            if (($entry.ExternalAttributes -shr 16 -band 0xF000) -eq 0xA000) { throw 'Archive links are not supported.' }
            $target = [System.IO.Path]::GetFullPath((Join-Path $Destination $name))
            if (-not $target.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Archive path escapes destination.' }
            if ($name.EndsWith('/')) { New-Item -ItemType Directory -Path $target -Force | Out-Null; continue }
            New-Item -ItemType Directory -Path (Split-Path $target -Parent) -Force | Out-Null
            [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $target, $false)
        }
    } finally { $zip.Dispose() }
}
function Install-DartsHub {
    if ($env:OS -ne 'Windows_NT') { throw 'Use install.sh for Linux/macOS.' }
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $architecture = [Environment]::GetEnvironmentVariable('PROCESSOR_ARCHITECTURE', 'Machine')
    $rid = switch ($architecture.ToUpperInvariant()) { 'AMD64' { 'win-x64' } 'ARM64' { 'win-arm64' } default { throw "Unsupported architecture: $architecture" } }
    Write-Host "DartsHub installer / Installation - $rid"
    if (-not $Channel) { $Channel = Read-Choice 'Channel / Kanal: stable, beta' 'stable' }
    if (-not $Mode) { $Mode = Read-Choice 'Mode / Betriebsart: gui, tui, headless' 'gui' }
    if ($Channel -notin @('stable', 'beta') -or $Mode -notin @('gui', 'tui', 'headless')) { throw 'Invalid channel or mode.' }
    if (-not $Directory) { $Directory = Read-Host "Install directory / Installationsordner [$env:LOCALAPPDATA\Programs\DartsHub]" }
    if ([string]::IsNullOrWhiteSpace($Directory)) { $Directory = Join-Path $env:LOCALAPPDATA 'Programs/DartsHub' }
    $Directory = [System.IO.Path]::GetFullPath($Directory)
    if ($Directory -eq [System.IO.Path]::GetPathRoot($Directory) -or $Directory -eq $env:USERPROFILE) { throw 'Choose a dedicated application directory.' }
    $autostart = Test-Yes (Read-Choice 'Autostart at login / Bei Anmeldung starten? yes/no' 'no')
    $minimized = $Mode -eq 'gui' -and $autostart -and (Test-Yes (Read-Choice 'Start minimized / Minimiert starten? yes/no' 'no'))
    if ($Mode -eq 'tui' -and $autostart) { Write-Host 'TUI autostart runs the headless backend; open the TUI shortcut to configure it.' }
    $headers = @{ 'User-Agent' = 'DartsHub-Installer'; Accept = 'application/vnd.github+json' }
    $releases = Invoke-RestMethod -Uri "https://api.github.com/repos/$Repository/releases?per_page=100" -Headers $headers -TimeoutSec 30
    $selected = Select-Release $releases ($Channel -eq 'beta') $rid
    $asset = $selected.Asset
    if (-not $asset.browser_download_url.StartsWith("https://github.com/$Repository/releases/download/", [StringComparison]::Ordinal)) { throw 'Unexpected download URL.' }
    if ($asset.digest -notmatch '^sha256:[0-9a-fA-F]{64}$') { throw 'Release has no SHA256 digest. Use a newly uploaded release.' }
    Write-Host "Installing $($selected.Release.tag_name) -> $Directory"
    if ((Test-Path -LiteralPath $Directory) -and -not (Test-Yes (Read-Choice 'Existing directory. Close DartsHub first. Continue? yes/no' 'no'))) { return }
    if (Test-Path -LiteralPath $Directory) {
        $items = @((Get-Item -LiteralPath $Directory -Force)) + @(Get-ChildItem -LiteralPath $Directory -Recurse -Force)
        if ($items | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }) { throw 'Installation directory contains links or junctions.' }
    }
    $work = Join-Path ([IO.Path]::GetTempPath()) ('dartshub-install-' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $work -Force | Out-Null
    try {
        $archive = Join-Path $work 'release.zip'
        Write-Host 'Downloading / Wird heruntergeladen ...'
        Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $archive -UseBasicParsing -TimeoutSec 300
        if ((Get-Item -LiteralPath $archive).Length -gt 1GB) { throw 'Archive exceeds 1 GB.' }
        if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash -ine $asset.digest.Substring(7)) { throw 'SHA256 mismatch. Installation canceled.' }
        $staging = Join-Path $work 'app'; New-Item -ItemType Directory -Path $staging | Out-Null
        Expand-SafeRelease $archive $staging
        if (-not (Test-Path -LiteralPath (Join-Path $staging 'DartsHub.exe') -PathType Leaf)) { throw 'Archive does not contain DartsHub.exe.' }
        New-Item -ItemType Directory -Path $Directory -Force | Out-Null
        Get-ChildItem -LiteralPath $staging -Force | Copy-Item -Destination $Directory -Recurse -Force
    } finally {
        $resolvedWork = [IO.Path]::GetFullPath($work)
        $tempRoot = [IO.Path]::GetFullPath([IO.Path]::GetTempPath()).TrimEnd('\') + '\'
        if (-not $resolvedWork.StartsWith($tempRoot, [StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid cleanup path.' }
        Remove-Item -LiteralPath $resolvedWork -Recurse -Force
    }
    $exe = Join-Path $Directory 'DartsHub.exe'
    $arguments = if ($Mode -eq 'gui') { if ($minimized) { '--minimized' } else { '' } } elseif ($Mode -eq 'tui') { '--tui' } else { '--headless --background' }
    $shell = New-Object -ComObject WScript.Shell
    $shortcutPath = Join-Path ([Environment]::GetFolderPath('Programs')) 'DartsHub.lnk'
    $shortcut = $shell.CreateShortcut($shortcutPath); $shortcut.TargetPath = $exe; $shortcut.Arguments = $arguments; $shortcut.WorkingDirectory = $Directory; $shortcut.Save()
    if ($autostart) {
        $target = if ($Mode -eq 'gui') { 'gui' } else { 'headless' }
        $startArguments = if ($target -eq 'headless') { '--headless --background' } elseif ($minimized) { '--minimized' } else { '' }
        New-Item -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -Force | Out-Null
        New-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -Name "DartsHub-$target" -Value ('"' + $exe + '" ' + $startArguments) -PropertyType String -Force | Out-Null
    }
    Write-Host "Installed / Installiert. Start menu: DartsHub. Path: $exe"
    if (-not $NoStart -and (Test-Yes (Read-Choice 'Start now / Jetzt starten? yes/no' 'yes'))) {
        if ($Mode -eq 'tui') { Start-Process -FilePath $exe -ArgumentList $arguments -WorkingDirectory $Directory -WindowStyle Normal }
        elseif ($arguments) { Start-Process -FilePath $exe -ArgumentList $arguments -WorkingDirectory $Directory -WindowStyle Hidden }
        else { Start-Process -FilePath $exe -WorkingDirectory $Directory -WindowStyle Hidden }
    }
}
if ($MyInvocation.InvocationName -ne '.') { Install-DartsHub }
