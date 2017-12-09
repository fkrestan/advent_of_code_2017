import typing
import re
import sys

from collections import defaultdict, Counter

# fwft(72) -> ktlj, cntj, xhth
RE_LINE = re.compile(r'(?P<name>\S+) \((?P<weight>\d+)\)(?: -> (?P<supports>.+))?')


def find_unbalanced(structure, root):
    supports = structure[root]['supports']
    weights = []

    for supported in supports:
        weight, unbalanced = find_unbalanced(structure, supported)

        if unbalanced:
            return None, unbalanced

        weights.append(weight)

    c = Counter(weights)

    if len(c) > 1:
        unique_weight = c.most_common()[-1][0]
        weight_difference = unique_weight - c.most_common()[0][0]
        idx = weights.index(unique_weight)
        unbalanced = supports[idx]
        needed_weight = structure[unbalanced]['weight'] - weight_difference

        return None, needed_weight

    return sum(weights) + structure[root]['weight'], None


def find_bottom_program(structure: dict):
    node = list(structure.keys())[0]

    while 'supported_by' in structure[node]:
        node = structure[node]['supported_by']

    return node


def parse_input(puzzle_input: typing.TextIO):
    structure = defaultdict(dict)

    for line in puzzle_input:
        program = RE_LINE.match(line).groupdict()

        structure[program['name']].update({
            'weight': int(program['weight']),
            'supports': program['supports'].split(', ') if program['supports'] is not None else []
        })

        for supports in structure[program['name']]['supports']:
            structure[supports]['supported_by'] = program['name']

    return structure


if __name__ == '__main__':
    file_name = 'input' if len(sys.argv) < 2 else  sys.argv[1]

    with open(file_name) as file:
        structure = parse_input(file)
        root = find_bottom_program(structure)
        print('Root: ' + root)
        print(find_unbalanced(structure, root))
