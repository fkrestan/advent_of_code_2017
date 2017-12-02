import sys
import io
from itertools import permutations


def line_checksum(line: str):
    line_int = [int(x) for x in line.split()]
    for x, y in permutations(line_int, 2):
        if x % y == 0:
            return x // y


def spreadsheet_checksum(spreadsheet: io.TextIOBase):
    return sum(line_checksum(line) for line in spreadsheet)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as spreadsheet:
        print(spreadsheet_checksum(spreadsheet))
