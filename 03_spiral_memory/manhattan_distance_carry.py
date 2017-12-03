from collections import namedtuple
import sys

Offset = namedtuple('Offset', ['x', 'y'])


def find_spiral_level(square: int):
    level = 0
    layer_side_size = 1

    while square > layer_side_size ** 2:
        layer_side_size += 2
        level += 1

    return level, layer_side_size


def manhattan_distance(offset: Offset):
    """Compute the Manhattan Distance to the square 1"""
    return abs(offset.x) + abs(offset.y)


def offset_on_spiral(square, level, side_size) -> Offset:
    """Compute an offset of given square from square 1"""
    # Spiral orientation does not matter
    # One direction is always level
    x = level

    side_first_square = side_size ** 2

    while square + side_size <= side_first_square:
        side_first_square -= side_size - 1

    # Distance from the side center
    y = abs(side_first_square - (side_size // 2) - square)

    return Offset(x, y)


def carry_distance(square):
    level, side_size = find_spiral_level(square)
    offset = offset_on_spiral(square, level, side_size)

    return manhattan_distance(offset)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(carry_distance(361527))
    else:
        print(carry_distance(int(sys.argv[1])))
