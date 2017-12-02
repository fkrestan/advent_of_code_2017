import sys


def solve_captcha(number: int):
    digits = [int(x) for x in str(number)]
    length = len(digits)

    return sum(digit for i, digit in enumerate(digits)
               if digit == digits[(i + length // 2) % length]
               )


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        number = int(file.read())

    print(solve_captcha(number))
