import pytest

import unique_words_passphrase
import unique_anagram_passphrase


@pytest.mark.parametrize('passphrase,valid', [
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True)
])
def test_valid_passphrase(passphrase, valid):
    assert unique_words_passphrase.valid_passphrase(passphrase) == valid


@pytest.mark.parametrize('passphrase,valid', [
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('a ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False)
])
def test_valid_anagram_passphrase(passphrase, valid):
    assert unique_anagram_passphrase.valid_passphrase(passphrase) == valid
