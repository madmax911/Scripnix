# Scripnix
Useful Python3 and bash shell scripts for macOS/BSD and \*NIX. Useful to me, at any rate. YMMV.

[![buildstatus](https://travis-ci.org/yukondude/Scripnix.svg?branch=master)](https://travis-ci.org/yukondude/Scripnix)
[![codecov](https://codecov.io/gh/yukondude/Scripnix/branch/master/graph/badge.svg)](https://codecov.io/gh/yukondude/Scripnix)
[![pypiversion](https://img.shields.io/pypi/v/Scripnix.svg)](https://pypi.python.org/pypi/Scripnix/)
[![licence](https://img.shields.io/pypi/l/Scripnix.svg)](https://pypi.python.org/pypi/Scripnix/)
[![pyversions](https://img.shields.io/pypi/pyversions/Scripnix.svg)](https://pypi.python.org/pypi/Scripnix/)
[![status](https://img.shields.io/pypi/status/Scripnix.svg)](https://pypi.python.org/pypi/Scripnix/)

Replaces the old [Scripnix0](https://github.com/yukondude/Scripnix0) project which had grown crufty and was not macOS-friendly.

## Licence

Licensed under the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html).
Refer to the attached LICENSE file or see <http://www.gnu.org/licenses/> for details.

## Version

`scripnix.__version__ == 0.1.4`

## Installation

*Homebrew and PyPI, eventually.*

## Commands

The following command descriptions were generated by `describe-scripnix` on October 26, 2016.

### `backup-file`
```
Usage: backup-file [OPTIONS] [FILE]...

  Backup the given file(s) by making a copy of each with an appended
  modification date (yyyymmdd). Append a number if the backup file name
  already exists. Remove any SUID or executable permissions from the backup
  file.

  The backup-file command is part of Scripnix.

Options:
  -D, --dry-run  Show what would happen without actually doing it.
  -V, --version  Show version and exit.
  -h, --help     Show this message and exit.
```

### `describe-scripnix`
```
Usage: describe-scripnix [OPTIONS]

  Generate descriptions of all of the Scripnix commands in Markdown format,
  suitable for appending to the Scripnix project's README.md file.

  The describe-scripnix command is part of Scripnix.

Options:
  -V, --version  Show version and exit.
  -h, --help     Show this message and exit.
```

### `gather-cron-jobs`
```
Usage: gather-cron-jobs [OPTIONS]

  Gather all of the system and user crontab schedules and display them in a
  consolidated tab-delimited table:

  mi hr dm mo dw user command

  The gather-cron-jobs command is part of Scripnix.

Options:
  -V, --version  Show version and exit.
  -h, --help     Show this message and exit.
```

### `hyphenate`
```
Usage: hyphenate [OPTIONS] [TEXT]...

  Translate the given text argument(s) (or use the input lines from STDIN)
  into the equivalent, filesystem-safe, hyphenated versions.

  The hyphenate command is part of Scripnix.

Options:
  -d, --delimiter TEXT  Word delimiter character(s).  [default: -]
  -V, --version         Show version and exit.
  -h, --help            Show this message and exit.
```

### `install-scripnix`
```
Usage: install-scripnix [OPTIONS]

  Install Scripnix for the current user. Global configuration settings (once
  installed by the root user) are stored under the /etc/scripnix/ directory.
  Per-user configuration settings, including for the root user, are stored
  under the ~/.scripnix/ directory and override the global settings. The
  installation can be re-run repeatedly, but will not overwrite existing
  configuration settings (however file and directory permissions will be
  reset).

  The install-scripnix command is part of Scripnix.

Options:
  --yes          Confirm the action without prompting.
  -v, --verbose  Display the commands as they are being executed.
  -D, --dry-run  Show what would happen without actually doing it.
  -V, --version  Show version and exit.
  -h, --help     Show this message and exit.
```
