import pytest

import jump_maze
import drunken_jump_maze


@pytest.mark.parametrize('position, maze, res_position, result_maze', [
    (0, [0, 3, 0, 1, -3], 0, [1, 3, 0, 1, -3]),
    (0, [1, 3, 0, 1, -3], 1, [2, 3, 0, 1, -3]),
    (1, [2, 3, 0, 1, -3], 4, [2, 4, 0, 1, -3]),
    (4, [2, 4, 0, 1, -3], 1, [2, 4, 0, 1, -2]),
    (1, [2, 4, 0, 1, -2], 5, [2, 5, 0, 1, -2])
])
def test_do_step(position, maze, res_position, result_maze):
    assert jump_maze.do_step(position, maze) == res_position
    assert maze == result_maze


@pytest.mark.parametrize('maze, steps', [
    ([0, 3, 0, 1, -3], 5)
])
def test_find_maze_exit(maze, steps):
    assert jump_maze.find_maze_exit(maze) == steps


@pytest.mark.parametrize('maze, steps, res_maze', [
    ([0, 3, 0, 1, -3], 10, [2, 3, 2, 3, -1])
])
def test_drunken_find_maze_exit(maze, steps, res_maze):
    assert drunken_jump_maze.find_maze_exit(maze) == steps
    assert maze == res_maze
