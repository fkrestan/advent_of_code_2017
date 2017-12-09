import io

import interpreter

input_instructions = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""


def test_interpret_lines():
    result = interpreter.interpret_instructions(io.StringIO(input_instructions))
    assert result == (1, 10)
