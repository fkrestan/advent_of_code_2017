from collections import defaultdict

import pytest

import stream_processor


@pytest.fixture
def fsm():
    return stream_processor.StramFSM()


def test_action_dict():
    did_action = False

    def action():
        nonlocal did_action
        did_action = True

    ad = stream_processor.ActionDict(
        lambda: 0,
        dictionary={1: 1, 2: 2},
        actions={2: action}
    )

    assert ad[999] == 0
    assert ad[1] == 1
    assert ad[2] == 2 and did_action == True


def test_action_dict_with_default_dict_action():
    did_action = False

    def action():
        nonlocal did_action
        did_action = True

    ad = stream_processor.ActionDict(
        lambda: 0,
        dictionary={1: 1},
        actions=defaultdict(lambda: action, {1: lambda: None})
    )

    assert ad[1] == 1 and did_action == False
    assert ad[2] == 0 and did_action == True


def run_fsm_states(fsm_, states):
    for symbols, expected_state in states:
        for symbol in symbols:
            fsm_.symbol(symbol)
            assert (fsm_.state, fsm_.group_depth, fsm_.score) == expected_state


def test_fsm_group_simple(fsm):
    # {}
    states = (
        ('{', ('group', 1, 1)),
        ('}', ('group', 0, 1))
    )

    run_fsm_states(fsm, states)


def test_fsm_group_nested(fsm):
    # {{{}}}
    states = (
        ('{', ('group', 1, 1)),
        ('{', ('group', 2, 3)),
        ('{', ('group', 3, 6)),
        ('}', ('group', 2, 6)),
        ('}', ('group', 1, 6)),
        ('}', ('group', 0, 6))
    )

    run_fsm_states(fsm, states)


def test_fsm_garbage_simple(fsm):
    # {<random characters>}
    states = (
        ('{', ('group', 1, 1)),
        ('<random characters', ('garbage', 1, 1)),
        ('>', ('group', 1, 1)),
        ('}', ('group', 0, 1))
    )

    run_fsm_states(fsm, states)


def test_fsm_garbage_ignored_group_end(fsm):
    # {<{!>}>}
    states = (
        ('{', ('group', 1, 1)),
        ('<{', ('garbage', 1, 1)),
        ('!', ('garbage_ignore_next', 1, 1)),
        ('>}', ('garbage', 1, 1)),
        ('>', ('group', 1, 1)),
        ('}', ('group', 0, 1))
    )

    run_fsm_states(fsm, states)


def test_fsm_garbage_repeated(fsm):
    states = (
        ('{', ('group', 1, 1)),
        ('<a', ('garbage', 1, 1)),
        ('>,', ('group', 1, 1)),
        ('<a', ('garbage', 1, 1)),
        ('>,', ('group', 1, 1)),
        ('<a', ('garbage', 1, 1)),
        ('>,', ('group', 1, 1)),
        ('<a', ('garbage', 1, 1)),
        ('>', ('group', 1, 1)),
        ('}', ('group', 0, 1))
    )

    run_fsm_states(fsm, states)


@pytest.mark.parametrize('stream,garbage_count', [
    ('{<>}', 0),
    ('{<random characters>}', 17),
    ('{<<<<>}', 3),
    ('{<{!>}>}', 2),
    ('{<!!>}', 0),
    ('{<!!!>>}', 0),
    ('{<{o"i!a,<{i<a>}', 10)
])
def test_fsm_garbage_repeated(stream, garbage_count, fsm):
    result = stream_processor.process_stream(stream)
    assert result.garbage_count == garbage_count
