import pytest

import knot_hash


@pytest.mark.parametrize('hashed_list,input_lengths,expected_hashed_list', [
    ([0, 1, 2, 3, 4], [3, 4, 1, 5], [3, 4, 2, 1, 0]),
])
def test_knot_hash_step(hashed_list, input_lengths, expected_hashed_list):
    knot_hash.knot_hash(input_lengths, hashed_list)

    assert hashed_list == expected_hashed_list


@pytest.mark.parametrize('hashed_list,current_position,input_length,expected_hashed_list', [
    ([0, 1, 2, 3, 4], 0, 3, [2, 1, 0, 3, 4]),
    ([2, 1, 0, 3, 4], 3, 4, [4, 3, 0, 1, 2]),
    ([4, 3, 0, 1, 2], 5, 1, [4, 3, 0, 1, 2]),
    ([4, 3, 0, 1, 2], 1, 5, [3, 4, 2, 1, 0]),
])
def test_reverse(hashed_list, current_position, input_length, expected_hashed_list):
    knot_hash.reverse(hashed_list, current_position, input_length)
    assert hashed_list == expected_hashed_list


def test_to_ascii_code():
    assert knot_hash.to_ascii_code('1,2,3') == [49, 44, 50, 44, 51]


def test_to_output_hex():
    assert knot_hash.to_output_hex([64, 7, 255]) == '4007ff'


def test_to_dense_hash_short():
    short_sparse_hash = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    dense_hash = knot_hash.to_dense_hash(short_sparse_hash)
    assert dense_hash == [64] + [0] * 15


def test_to_dense_hash_long():
    full_sparse_hash = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22] * 16
    dense_hash = knot_hash.to_dense_hash(full_sparse_hash)
    assert dense_hash == [64] * 16


@pytest.mark.parametrize('input_string,expected_hex_digest', [
    ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
    ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
    ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
    ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
])
def test_hex_digest(input_string, expected_hex_digest):
    h = knot_hash.KnotHash(input_string)
    hex_digest = h.hex_digest()
    assert hex_digest == expected_hex_digest
