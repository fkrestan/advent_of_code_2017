import sys
from functools import reduce


def reverse(hashed_list, current_position, length):
    for i in range(length // 2):
        fow_i = (current_position + i) % len(hashed_list)
        rev_i = (current_position + length - i - 1) % len(hashed_list)
        hashed_list[fow_i], hashed_list[rev_i] = hashed_list[rev_i], hashed_list[fow_i]


def to_ascii_code(input_string):
    return [ord(x) for x in input_string]


def to_dense_hash(sparse_hash):
    sparse_hash += [0] * (256 - len(sparse_hash))  # Pad with 0s to len == 256

    return [reduce(lambda x, y: x ^ y, sparse_hash[i:i + 16]) for i in range(0, 256, 16)]


def to_output_hex(dense_hash):
    hex_hash = 0

    for i in dense_hash:
        hex_hash = (hex_hash << 8) + i

    return hex(hex_hash).lstrip('0x')


class KnotHash:
    def __init__(self, input_lengths, hashed_list=None):
        if isinstance(input_lengths, str):
            input_lengths = to_ascii_code(input_lengths)

        input_lengths += [17, 31, 73, 47, 23]

        if hashed_list is None:
            hashed_list = list(range(256))

        self._current_position = 0
        self._skip_size = 0
        self.input_lengths = input_lengths
        self.hashed_list = hashed_list
        self.dense_hash = None

    def _knot_hash_step(self):
        for length in self.input_lengths:
            reverse(self.hashed_list, self._current_position, length)
            self._current_position += length + self._skip_size
            self._skip_size += 1

    def hex_digest(self):
        if self.dense_hash is None:
            for i in range(64):
                self._knot_hash_step()

            self.dense_hash = to_dense_hash(self.hashed_list)

        return to_output_hex(self.dense_hash)


def knot_hash(input_lenghts, hashed_list=None):
    """Part One - return multiplied two first numbers of first knot hash iteration"""
    if hashed_list is None:
        hashed_list = list(range(256))

    current_position = 0
    skip_size = 0

    for length in input_lenghts:
        reverse(hashed_list, current_position, length)
        current_position += length + skip_size
        skip_size += 1

    return hashed_list[0] * hashed_list[1]


if __name__ == '__main__':
    if __name__ == '__main__':
        file_name = 'input' if len(sys.argv) < 2 else sys.argv[1]

        with open(file_name) as file:
            input_string = file.read()
            print(knot_hash([int(x) for x in input_string.split(',')]))

            kh = KnotHash(input_string.strip())
            print(kh.hex_digest())
