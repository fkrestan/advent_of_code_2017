import sys


def solve_captcha(number: int):
    digits = [int(x) for x in str(number)]
    digits.append(digits[0])

    return sum(x for x, y in zip(digits[0:], digits[1:]) if x == y)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        number = int(file.read())

    print(solve_captcha(number))
