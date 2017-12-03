import pytest

import manhattan_distance_carry


@pytest.mark.parametrize("square,spiral_level,side_size", [
    (1, 0, 1),
    (9, 1, 3),
    (10, 2, 5),
    (12, 2, 5),
    (23, 2, 5),
    (25, 2, 5),
    (26, 3, 7)
])
def test_find_spiral_level(square, spiral_level, side_size):
    test_level, test_size = manhattan_distance_carry.find_spiral_level(square)
    assert (test_level, test_size) == (spiral_level, side_size)


@pytest.mark.parametrize("square,spiral_level,side_size,offset", [
    (1, 0, 1, manhattan_distance_carry.Offset(0, 0)),
    (9, 1, 3, manhattan_distance_carry.Offset(1, 1)),
    (10, 2, 5, manhattan_distance_carry.Offset(2, 1)),
    (12, 2, 5, manhattan_distance_carry.Offset(2, 1)),
    (23, 2, 5, manhattan_distance_carry.Offset(2, 0)),
    (25, 2, 5, manhattan_distance_carry.Offset(2, 2)),
    (26, 3, 7, manhattan_distance_carry.Offset(3, 2))
])
def test_offset_on_spiral(square, spiral_level, side_size, offset):
    o = manhattan_distance_carry.offset_on_spiral(square, spiral_level, side_size)
    assert o == offset


@pytest.mark.parametrize("square,manhattan_distance", [
    (1, 0),
    (9, 2),
    (10, 3),
    (12, 3),
    (23, 2),
    (25, 4),
    (26, 5),
    (1024, 31)
])
def test_carry_distance(square, manhattan_distance):
    distance = manhattan_distance_carry.carry_distance(square)
    assert distance == manhattan_distance
