import sys
from collections import deque


def parse_plumbing(plumbing):
    connections = dict()

    for i in plumbing.splitlines():
        node, pipes = i.split(' <-> ')
        node = int(node)
        pipes = {int(x) for x in pipes.split(', ')}
        connections[node] = pipes

    return connections


def bfs(connections, start_node=0):
    open_ = deque([start_node])
    closed = set()

    while len(open_) > 0:
        node = open_.pop()

        neighbors = connections[node]
        open_.extendleft(neighbors.difference(closed))
        closed.add(node)

    return closed


def group_size(plumbing):
    connections = parse_plumbing(plumbing)
    return len(bfs(connections))


def group_count(plumbing):
    connections = parse_plumbing(plumbing)
    programs = set(connections.keys())
    program = 0
    count = 1

    while True:
        group = bfs(connections, program)
        programs -= group
        try:
            program = programs.pop()
            count += 1
        except KeyError:
            break

    return count


if __name__ == '__main__':
    file_name = 'input' if len(sys.argv) < 2 else sys.argv[1]

    with open(file_name) as file:
        plumbing_input = file.read()
        print(group_size(plumbing_input))
        print(group_count(plumbing_input))
