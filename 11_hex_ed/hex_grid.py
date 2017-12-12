"""
Implementation of Chris Schetters hex grid
See http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
"""

import sys
from collections import namedtuple

directions = {
    'n': (1, 0),
    's': (-1, 0),
    'nw': (0, 1),
    'se': (0, -1),
    'ne': (1, -1),
    'sw': (-1, 1)
}

_QBertCoordinate = namedtuple('QBertCoordinate', ['x', 'y'])


class QBertCoordinate(_QBertCoordinate):
    def __add__(self, other):
        return QBertCoordinate(self.x + other[0], self.y + other[1])


def z_qbert_coordinate(coordinate: QBertCoordinate):
    return - (coordinate.x + coordinate.y)


def distance(coordinate):
    return max(abs(coordinate.x), abs(coordinate.y), abs(z_qbert_coordinate(coordinate)))


def walk_path(path):
    position = QBertCoordinate(0, 0)

    for step in path:
        position += directions[step]

    return position


def path_max_distance(path):
    position = QBertCoordinate(0, 0)
    max_distance = 0

    for step in path:
        position = position + directions[step]
        max_distance = max(max_distance, distance(position))

    return max_distance


def parse_path_spec(path_spec):
    return path_spec.strip().split(',')


if __name__ == '__main__':
    if __name__ == '__main__':
        file_name = 'input' if len(sys.argv) < 2 else sys.argv[1]

        with open(file_name) as file:
            path = parse_path_spec(file.read())
            position = walk_path(path)
            print(distance(position))
            print(path_max_distance(path))
