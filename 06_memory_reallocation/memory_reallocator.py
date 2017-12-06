import operator
import sys


def repeated_state(memory: list):
    idx, amount = max(enumerate(memory), key=operator.itemgetter(1))
    memory_len = len(memory)

    states = set(tuple(memory))
    count = 0

    while True:
        quotient, remainder = divmod(amount, memory_len)
        memory[idx] = 0
        next_amount = 0
        next_idx = 0

        for i in range(memory_len):
            memory[i] += quotient + ((amount + remainder - (i + idx - 1) % memory_len - 1) // amount)
            if memory[i] > next_amount:
                next_amount = memory[i]
                next_idx = i

        count += 1

        if tuple(memory) not in states:
            states.add(tuple(memory))
        else:
            return count

        amount = next_amount
        idx = next_idx


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            memory = [int(i) for i in file.read().split()]
            print(repeated_state(memory))
    else:
        print(repeated_state([2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]))
