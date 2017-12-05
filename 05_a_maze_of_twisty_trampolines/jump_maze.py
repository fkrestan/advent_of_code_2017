import sys


def do_step(position, maze):
    res_position = position + maze[position]
    maze[position] += 1

    return res_position


def find_maze_exit(maze):
    steps = 0
    position = 0

    while 0 <= position < len(maze):
        steps += 1
        position = do_step(position, maze)

    return steps


def parse_maze(filename):
    with open(filename) as file:
        maze = [int(l.strip()) for l in file]

    return maze


if __name__ == '__main__':
    print(find_maze_exit(parse_maze(sys.argv[1])))
