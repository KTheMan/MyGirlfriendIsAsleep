#!/usr/bin/env python3

import sys
import os
import platform
import subprocess
import time
import datetime

def install_dependency(dep_name):
    if dep_name == "nircmd":
        try:
            subprocess.run(["winget", "install", "nircmd"], check=True)
        except subprocess.CalledProcessError:
            print("Failed to install nircmd using winget. Please manually download nircmd from https://www.nirsoft.net/utils/nircmd.html and place it in a directory in your PATH or the current directory.")
    elif dep_name == "caffeinate":
        print("caffeinate should be preinstalled on macOS. Please ensure it's available.")
    elif dep_name == "xset":
        subprocess.run(["sudo", "apt-get", "install", "x11-xserver-utils"])

def check_dependency(dep_name):
    try:
        subprocess.run([dep_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

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
        print("Usage: mygirlfriendisasleep [off/on/shesasleepuntil HH:MM]")
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
