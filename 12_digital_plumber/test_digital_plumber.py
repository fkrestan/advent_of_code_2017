import pytest

import plumb

plumbing_input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


@pytest.fixture()
def plumbing():
    return plumb.parse_plumbing(plumbing_input)


def test_parse_plumbing():
    p = plumb.parse_plumbing(plumbing_input)

    assert isinstance(p, dict)
    assert len(p) == 7
    assert p['2'] == {'0', '3', '4'}


def test_bfs(plumbing):
    res_set = plumb.bfs(plumbing)
    assert res_set == {'0', '2', '3', '4', '5', '6'}


def test_group_size():
    res_size = plumb.group_size(plumbing_input)
    assert res_size == 6


def test_group_count():
    count = plumb.group_count(plumbing_input)
    assert count == 2
