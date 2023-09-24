# My Girlfriend Is Asleep

`MyGirlfriendIsAsleep` is a cross-platform script designed to help users turn off their physical displays with the option to automatically turn them back on at a specified time. Especially useful when you want to keep your room dark while streaming content!

[![Build and Release](https://github.com/KTheMan/MyGirlfriendIsAsleep/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/KTheMan/MyGirlfriendIsAsleep/actions/workflows/build-and-release.yml)

## Features

- **Cross-Platform**: Works on Windows and Linux. Potential macOS support in the future
- **Dependency Checks**: Automatically verifies the presence of required tools and provides installation guidance.
- **Delayed Monitor Activation**: With the `--shesasleepuntil` flag, set a specific time for the monitors to reactivate. Use `--force` to turn on the display before the set time.

## Usage

To can run the executable:

- **Turn off the display**: 
  ```bash
  ./mygirlfriendisasleep off
  ```

- **Turn on the display**:
  ```bash
  ./mygirlfriendisasleep on
  ```

- **Turn off the display and turn it back on at a specified time (e.g., 2:25 PM)**:
  ```bash
  ./mygirlfriendisasleep off --shesasleepuntil 14:25
  ```

- **Turn on the display forcibly (useful after setting a `--shesasleepuntil` time)**:
  ```bash
  ./mygirlfriendisasleep on --force
  ```

## Dependencies

This script interacts with or can trigger the installation of the following software:

1. **nircmd** (Windows)
   - **Description**: A command-line utility for various tasks without a user interface.
   - **License**: Freeware by NirSoft. Redistribution is permitted, but selling without permission is prohibited.
   - [NirSoft nircmd](https://www.nirsoft.net/utils/nircmd.html)

2. **caffeinate** (macOS)
   - **Description**: A built-in macOS command to prevent the system from sleeping.
   - **License**: Part of Apple's proprietary macOS. No redistribution.

3. **xset** (Linux)
   - **Description**: A utility from the `x11-xserver-utils` package, providing user access to several X server settings.
   - **License**: Typically under the MIT License.
   - [X.Org xset](https://www.x.org/releases/X11R7.7/doc/man/man1/xset.1.xhtml)

## Licensing

`MyGirlfriendIsAsleep` is licensed under the LGPLv3. Please adhere to the terms of the LGPLv3 when using or redistributing this software.

Third-party tools that the script interacts with have their own licenses, as detailed above. While the script does not redistribute any third-party software, it can facilitate their installation or usage.

## Contributing

Contributions, suggestions, and issues are welcome! Open an issue or pull request on the project's repository.

---

*Developed with ❤️ by [KTheMan](knnygrdn.com).*
