import sys
import io


def line_checksum(line: str):
    line_int = [int(x) for x in line.split()]
    return max(line_int) - min(line_int)


def spreadsheet_checksum(spreadsheet: io.TextIOBase):
    return sum(line_checksum(line) for line in spreadsheet)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as spreadsheet:
        print(spreadsheet_checksum(spreadsheet))
