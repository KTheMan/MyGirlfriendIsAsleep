#!/usr/bin/env python3

import sys
import os
import platform
import subprocess
import time
import datetime
import requests

def install_dependency(dep_name):
    if dep_name == "nircmd":
        try:
            subprocess.run(["winget", "install", "gerardog.gsudo"])
            refresh_environment()
            subprocess.run(["gsudo", "winget", "install", "nircmd"], check=True)
            refresh_environment()
        except subprocess.CalledProcessError:
            print("Failed to install nircmd using winget. Please manually download nircmd from https://www.nirsoft.net/utils/nircmd.html and place it in a directory in your PATH or the current directory.")
    elif dep_name == "caffeinate":
        print("caffeinate should be preinstalled on macOS. Please ensure it's available.")
    elif dep_name == "xset":
        cmd = ["sudo", "apt-get", "install", "x11-xserver-utils"] if not is_elevated() else ["apt-get", "install", "x11-xserver-utils"]
        subprocess.run(cmd)

def check_dependency(dep_name):
    try:
        if dep_name == "nircmd":
            result = subprocess.run(["winget", "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if "nircmd" in result.stdout:
                return True

        elif dep_name == "xset":
            result = subprocess.run(["dpkg", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if "x11-xserver-utils" in result.stdout:
                return True

        else:
            subprocess.run([dep_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True

    except Exception as e:
        print(f"Error checking dependency {dep_name}: {e}")
        return False

    return False

import os
import subprocess

def refresh_environment():
    ps_script = '''
    $userName = $env:USERNAME
    $architecture = $env:PROCESSOR_ARCHITECTURE
    $psModulePath = $env:PSModulePath

    $ScopeList = 'Process', 'Machine'
    if ($userName -notin 'SYSTEM', "${env:COMPUTERNAME}`$") {
        $ScopeList += 'User'
    }
    foreach ($Scope in $ScopeList) {
        Get-ChildItem -Path "Env:" | ForEach-Object {
            $envVarName = $_.Name
            Set-Item "Env:$envVarName" -Value ([System.Environment]::GetEnvironmentVariable($envVarName, $Scope))
        }
    }

    $paths = 'Machine', 'User' | ForEach-Object {
        ([System.Environment]::GetEnvironmentVariable('PATH', $_)) -split ';'
    } | Select-Object -Unique
    $Env:PATH = $paths -join ';'

    $env:PSModulePath = $psModulePath

    if ($userName) { $env:USERNAME = $userName; }
    if ($architecture) { $env:PROCESSOR_ARCHITECTURE = $architecture; }
    '''

    # Execute the PowerShell script
    result = subprocess.run(['powershell', '-Command', ps_script], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error occurred: {result.stderr}")
    else:
        print("Environment updated in PowerShell session!")

    # Update PATH in the current Python environment
    fetch_updated_path()

def fetch_updated_path():
    # Fetch the updated PATH using PowerShell
    cmd = 'powershell -Command "[System.Environment]::GetEnvironmentVariable(\'PATH\', \'Machine\')"'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    
    # Split both old PATH and new PATH into lists
    old_path = set(os.environ['PATH'].split(';'))
    new_path = set(result.stdout.strip().split(';'))
    
    # Update the old PATH with entries from the new PATH
    combined_path = old_path.union(new_path)
    os.environ['PATH'] = ';'.join(combined_path)

    print("Environment updated in Python!")

def turn_off_display():
    sys_platform = platform.system()

    if sys_platform == "Windows":
        if not check_dependency("nircmd"):
            install_dependency("nircmd")
        subprocess.run(["nircmd", "monitor", "off"])

    elif sys_platform == "Darwin":
        if not check_dependency("caffeinate"):
            install_dependency("caffeinate")
        subprocess.run(["caffeinate", "-u", "-t", "1"])

    elif sys_platform == "Linux":
        if not check_dependency("xset"):
            install_dependency("xset")
        subprocess.run(["xset", "dpms", "force", "off"])

def turn_on_display():
    sys_platform = platform.system()

    if sys_platform == "Windows":
        if not check_dependency("nircmd"):
            install_dependency("nircmd")
        subprocess.run(["nircmd", "monitor", "on"])

    elif sys_platform == "Linux":
        if not check_dependency("xset"):
            install_dependency("xset")
        subprocess.run(["xset", "dpms", "force", "on"])

def main():
    force_turn_on = "--force" in sys.argv
    set_sleep_time = "--shesasleepuntil" in sys.argv
    turn_on_cmd = "on" in sys.argv

    if len(sys.argv) < 2:
        print("Usage: mygirlfriendisasleep [off/on] [off arguments: --shesasleepuntil HH:MM] [on arguments: --force]")
        return

    if turn_on_cmd and not force_turn_on and set_sleep_time:
        print("Use --force to turn on the display before the set time.")
        return

    if turn_on_cmd and force_turn_on:
        turn_on_display()
        return

    if "off" in sys.argv:
        turn_off_display()
        if set_sleep_time:
            time_idx = sys.argv.index("--shesasleepuntil") + 1
            if time_idx < len(sys.argv):
                target_time_str = sys.argv[time_idx]
                target_time = datetime.datetime.strptime(target_time_str, "%H:%M").time()
                now = datetime.datetime.now().time()

                while now < target_time:
                    time.sleep(60)
                    now = datetime.datetime.now().time()

                turn_on_display()

if __name__ == "__main__":
    main()
