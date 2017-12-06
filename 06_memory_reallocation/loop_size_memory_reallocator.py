import operator
import sys


def repeated_state_loop_size(memory: list):
    idx, amount = max(enumerate(memory), key=operator.itemgetter(1))
    memory_len = len(memory)

    states = {tuple(memory): 0}
    count = 0

    while True:
        quotient, remainder = divmod(amount, memory_len)
        memory[idx] = 0
        next_amount = 0
        next_idx = memory_len

        for i in range(1, memory_len + 1):
            idx = (idx + 1) % memory_len
            memory[idx] += quotient + (amount + remainder - i) // amount

            if memory[idx] > next_amount or (memory[idx] == next_amount and idx < next_idx):
                next_amount = memory[idx]
                next_idx = idx

        count += 1

        if tuple(memory) not in states.keys():
            states[tuple(memory)] = count
        else:
            return count - states[tuple(memory)]

        amount = next_amount
        idx = next_idx


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            memory = [int(i) for i in file.read().split()]
            print(repeated_state_loop_size(memory))
    else:
        print(repeated_state_loop_size([2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]))
