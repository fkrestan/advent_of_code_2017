import pytest
import io

import line_max_difference_checksum
import line_divmod_checksum


@pytest.mark.parametrize("line,checksum", [
    ('5 1 9 5', 8),
    ('7 5 3', 4),
    ('2 4 6 8', 6)
])
def test_line_checksum_given_input(line, checksum):
    assert line_max_difference_checksum.line_checksum(line) == checksum


def test_spreadsheet_checksum_given_input():
    spreadsheet = io.StringIO('5 1 9 5\n7 5 3\n2 4 6 8')
    assert line_max_difference_checksum.spreadsheet_checksum(spreadsheet) == 18


@pytest.mark.parametrize("line,checksum", [
    ('5 9 2 8', 4),
    ('9 4 7 3', 3),
    ('3 8 6 5', 2)
])
def test_line_divmod_checksum_given_input(line, checksum):
    assert line_divmod_checksum.line_checksum(line) == checksum


def test_spreadsheet_divmod_checksum_given_input():
    spreadsheet = io.StringIO('5 9 2 8\n9 4 7 3\n3 8 6 5')
    assert line_max_difference_checksum.spreadsheet_checksum(spreadsheet) == 18
