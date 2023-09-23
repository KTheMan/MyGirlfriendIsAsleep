# Changelog

All notable changes to "My Girlfriend Is Asleep" will be documented in this file.

## [Unreleased Template]

### Added
- 

### Changed
- 

### Deprecated
- 

### Removed
- 

### Fixed
- 

### Security
- 

## [1.0.0] - 2023-09-23

### Added

- Cross-platform support for Windows, macOS, and Linux.
- Automatic detection of platform and required tools.
- `--shesasleepuntil` flag to specify monitor reactivation time.
- Force activation of the monitor even if `--shesasleepuntil` is set.
- CI/CD pipeline for automated building and releasing of executables.

---

## Instructions for Updating the Changelog

1. **For Ongoing Changes**: As you make changes in between releases, document them under the "Unreleased" section. Group them by type: "Added", "Changed", "Deprecated", "Removed", "Fixed", and "Security".
2. **For a New Release**: 
   - Move everything under the "Unreleased" section to a new version section.
   - Update the version number and the date.
   - Start a new "Unreleased" section for the next set of changes.
   - Always keep the changelog in reverse chronological order.
3. **Committing**: Whenever you update the changelog, commit it to your version control system so you have a historical record of changes.
4. **Formatting**: Use the provided template structure for consistency. Users and developers rely on the changelog's consistency to quickly understand changes.
