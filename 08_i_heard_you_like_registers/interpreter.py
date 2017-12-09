import sys
from collections import defaultdict, namedtuple

InterpretationResult = namedtuple('InterpretationResult', ['max_current', 'max_in_run'])


class Interpreter:
    def __init__(self):
        self.registers = defaultdict(lambda: 0)
        self.max_in_run = 0

    def interpret_line(self, line):
        operation, condition = line.split(' if ')

        if eval(condition, dict(), self.registers):
            operation = operation.replace('inc', '+=')
            operation = operation.replace('dec', '-=')
            exec(operation, dict(), self.registers)

            self.max_in_run = max(self.max_value(), self.max_in_run)

    def max_value(self):
        return max(self.registers.values())


def interpret_instructions(instructuions):
    interpreter = Interpreter()

    for line in instructuions:
        interpreter.interpret_line(line)

    return InterpretationResult(interpreter.max_value(), interpreter.max_in_run)


if __name__ == '__main__':
    file_name = 'input' if len(sys.argv) < 2 else sys.argv[1]

    with open(file_name) as file:
        print(interpret_instructions(file))
