import io
import sys


def unique_words(word_list: list):
    return set(word_list)


def valid_passphrase(passphrase: str):
    word_list = passphrase.split()
    unique = unique_words(word_list)

    return len(word_list) == len(unique)


def valid_passphrase_count(passphrases: io.TextIOBase) -> int:
    return sum(1 for p in passphrases if valid_passphrase(p))


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(valid_passphrase_count(file))
