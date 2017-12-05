import sys

from jump_maze import parse_maze


def do_step(position, maze):
    offset = maze[position]
    res_position = position + offset
    maze[position] += 1 if offset < 3 else -1

    return res_position


def find_maze_exit(maze):
    steps = 0
    position = 0

    while 0 <= position < len(maze):
        steps += 1
        position = do_step(position, maze)

    return steps


if __name__ == '__main__':
    print(find_maze_exit(parse_maze(sys.argv[1])))
