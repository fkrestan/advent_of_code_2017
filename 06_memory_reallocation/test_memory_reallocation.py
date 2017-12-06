import pytest

import memory_reallocator
import loop_size_memory_reallocator


@pytest.mark.parametrize('current_state,repeated_state,step_count', [
    ([0, 2, 7, 0], [2, 4, 1, 2], 5),
])
def test_repeated_state(current_state, repeated_state, step_count):
    assert memory_reallocator.repeated_state(current_state) == step_count
    assert current_state == repeated_state


@pytest.mark.parametrize('current_state,repeated_state,step_count', [
    ([0, 2, 7, 0], [2, 4, 1, 2], 4),
])
def test_repeated_state_loop_size(current_state, repeated_state, step_count):
    assert loop_size_memory_reallocator.repeated_state_loop_size(current_state) == step_count
    assert current_state == repeated_state
