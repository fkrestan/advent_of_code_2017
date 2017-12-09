import io

import bottom_program

test_input = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""

test_input_names = [
    'pbga',
    'xhth',
    'ebii',
    'havc',
    'ktlj',
    'fwft',
    'qoyq',
    'padx',
    'tknk',
    'jptl',
    'ugml',
    'gyxo',
    'cntj'
]


def test_parse_input():
    structure = bottom_program.parse_input(io.StringIO(test_input))
    assert set(structure.keys()) == set(test_input_names)
    assert set(structure['ugml']['supports']) == {'gyxo', 'ebii', 'jptl'}
    assert structure['ugml']['supported_by'] == 'tknk'
    assert structure['cntj']['weight'] == 57


def test_find_bottom_program():
    structure = bottom_program.parse_input(io.StringIO(test_input))
    assert bottom_program.find_bottom_program(structure) == 'tknk'


def test_find_unbalanced():
    structure = bottom_program.parse_input(io.StringIO(test_input))
    root = bottom_program.find_bottom_program(structure)
    unbalanced = bottom_program.find_unbalanced(structure, root)
    assert unbalanced == (None, 60)
