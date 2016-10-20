""" Scripnix backup-file command unit tests
"""

# This file is part of Scripnix. Copyright 2016 Dave Rogers <info@yukondude.com>. Licensed under the GNU General Public License, version 3.
# Refer to the attached LICENSE file or see <http://www.gnu.org/licenses/> for details.

from click.testing import CliRunner
import datetime
import os
# noinspection PyPackageRequirements
import pytest
import time
from scripnix.pycommand.backup_file import assemble_dry_run_message, Backup, collect_backups, COMMAND_NAME, execute_backups, main
from .common_options import common_help_option, common_version_option


DRY_RUN_PREFIX = "{} would do the following:".format(COMMAND_NAME)


def test_backup_file_help_option():
    common_help_option(command_entry=main, command_name=COMMAND_NAME)


@pytest.mark.parametrize('backups,expected', [
    ([], DRY_RUN_PREFIX),
    ([Backup('foo', 'foo.1', False)], "\n".join([DRY_RUN_PREFIX, "cp foo foo.1"])),
    ([Backup('bar', 'bar.1', True)], "\n".join([DRY_RUN_PREFIX, "cp bar bar.1", "chmod -x,u-s bar.1"])),
    ([Backup('foo', 'foo.1', False), Backup('bar', 'bar.1', True)], "\n".join([DRY_RUN_PREFIX, "cp foo foo.1", "cp bar bar.1", "chmod -x,u-s bar.1"])),
])
def test_backup_file_assemble_dry_run_message(backups, expected):
    assert assemble_dry_run_message(backups=backups) == expected


def test_backup_file_version_option():
    common_version_option(command_entry=main, command_name=COMMAND_NAME)


@pytest.mark.parametrize('file_name_permissions,expected', [
    ([], []),
    ([("test.tst", 0o0644)], [Backup("test.tst", "test.tst.20140702", False)]),
    ([("test.exe", 0o0755)], [Backup("test.exe", "test.exe.20140702", True)]),
    ([("test.suid", 0o4644)], [Backup("test.suid", "test.suid.20140702", True)]),
    ([("test.tst", 0o0644), ("test.exe", 0o0755)],
     [Backup("test.tst", "test.tst.20140702", False), Backup("test.exe", "test.exe.20140702", True)]),
    ([("test.tst", 0o0644), ("test.tst.20140702", 0o0644)],
     [Backup("test.tst", "test.tst.20140702.1", False), Backup("test.tst.20140702", "test.tst.20140702.20140702", False)]),
])
def test_backup_file_collect_backups(file_name_permissions, expected):
    with CliRunner().isolated_filesystem():
        for file_name, mode in file_name_permissions:
            with open(file_name, "a"):
                os.utime(file_name, (time.time(), datetime.datetime(2014, 7, 2, 0, 0).timestamp()))
            os.chmod(file_name, mode)

        test_path = os.path.abspath(".")

        backups = collect_backups([f[0] for f in file_name_permissions])
        assert len(backups) == len(expected)

        for i, backup in enumerate(backups):
            assert backup.from_path == os.path.join(test_path, expected[i].from_path)
            assert backup.to_path == os.path.join(test_path, expected[i].to_path)
            assert backup.is_exec_or_suid == expected[i].is_exec_or_suid


@pytest.mark.parametrize('file_name_permissions,expected', [
    ([], []),
    ([("test.tst", 0o0644)], [("test.tst", 0o100644), ("test.tst.20120616", 0o100644)]),
    ([("test.exe", 0o0755)], [("test.exe", 0o100755), ("test.exe.20120616", 0o100644)]),
    ([("test.suid", 0o4644)], [("test.suid", 0o104644), ("test.suid.20120616", 0o100644)]),
    ([("test.suid", 0o4750)], [("test.suid", 0o104750), ("test.suid.20120616", 0o100640)]),
])
def test_backup_file_execute_backups_success(file_name_permissions, expected):
    with CliRunner().isolated_filesystem():
        for file_name, mode in file_name_permissions:
            with open(file_name, "a"):
                os.utime(file_name, (time.time(), datetime.datetime(2012, 6, 16, 0, 0).timestamp()))
            os.chmod(file_name, mode)

        backups = collect_backups([f[0] for f in file_name_permissions])
        execute_backups(backups)

        # Make sure unexpected files weren't somehow created.
        assert len(os.listdir(".")) == len(expected)

        for file_name, mode in expected:
            assert os.path.isfile(file_name)
            assert os.stat(file_name).st_mode == mode

