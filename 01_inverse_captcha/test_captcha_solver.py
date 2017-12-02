import pytest

import consecutive_captcha
import halfway_around_captcha


@pytest.mark.parametrize("number,expected_sum", [
    (1122, 3),
    (1111, 4),
    (1234, 0),
    (91212129, 9)
])
def test_consecutive_captcha_given_input(number, expected_sum):
    assert consecutive_captcha.solve_captcha(number) == expected_sum


def test_consecutive_negative_input():
    with pytest.raises(ValueError):
        consecutive_captcha.solve_captcha(-111)


@pytest.mark.parametrize("number,expected_sum", [
    (1212, 6),
    (1221, 0),
    (123425, 4),
    (123123, 12),
    (12131415, 4)
])
def test_halfway_around_captcha_given_input(number, expected_sum):
    assert halfway_around_captcha.solve_captcha(number) == expected_sum
