import sys
import os
import urllib.request
import contextlib

"""See https://oeis.org/A094769

This is just a tool that downloads precomputed sequence 
from http://oeis.org/A141481/b141481.txt and finds the result. 
"""

sequence_file_url = 'http://oeis.org/A141481/b141481.txt'
sequence_file_name = os.path.join(os.path.dirname(__file__), 'sequence.txt')


def filter_sequence_file(line: str):
    return not (line.startswith('#') or line.strip() == '')


def map_sequence_file(line: str):
    return int(line.split()[1])


@contextlib.contextmanager
def sequence(file_name: str):
    if not os.path.isfile(file_name):
        urllib.request.urlretrieve(sequence_file_url, file_name)

    with open(file_name) as file:
        valid_lines = filter(filter_sequence_file, file)
        values = map(map_sequence_file, valid_lines)
        yield values


def first_larger(value: int):
    with sequence(sequence_file_name) as s:
        for val in s:
            if val > value:
                return val


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(first_larger(361527))
    else:
        print(first_larger(int(sys.argv[1])))
