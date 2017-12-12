import pytest

import hex_grid


@pytest.mark.parametrize('coordinate,expected_z', [
    (hex_grid.QBertCoordinate(0, 0), 0),
    (hex_grid.QBertCoordinate(1, 0), -1),
    (hex_grid.QBertCoordinate(0, 1), -1),
    (hex_grid.QBertCoordinate(1, 1), -2),
])
def test_z_qbert_coordinate(coordinate, expected_z):
    z = hex_grid.z_qbert_coordinate(coordinate)

    assert z == expected_z


@pytest.mark.parametrize('path,expected_position', [
    (['ne', 'ne', 'ne'], (3, -3)),
    (['ne', 'ne', 'sw', 'sw'], (0, 0)),
    (['ne', 'ne', 's', 's'], (0, -2)),
    (['se', 'sw', 'se', 'sw', 'sw'], (-3, 1)),
])
def test_walk_path(path, expected_position):
    position = hex_grid.walk_path(path)
    assert position == expected_position


@pytest.mark.parametrize('path,expected_distance', [
    (['ne', 'ne', 'ne'], 3),
    (['ne', 'ne', 'sw', 'sw'], 0),
    (['ne', 'ne', 's', 's'], 2),
    (['se', 'sw', 'se', 'sw', 'sw'], 3),
])
def test_distance(path, expected_distance):
    position = hex_grid.walk_path(path)
    distance = hex_grid.distance(position)
    assert distance == expected_distance
