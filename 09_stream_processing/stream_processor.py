from collections import defaultdict, namedtuple
import sys

FSMResult = namedtuple('FSMResult', ['score', 'garbage_count'])


class ActionDict(defaultdict):
    def __init__(self, default, dictionary, actions):
        super().__init__(default, dictionary)
        self.actions = actions

    def __getitem__(self, key):
        try:
            # defaultdict(lambda: 0).get(5, 42) -> 42
            action = self.actions[key]
            action()
        except KeyError:
            pass
        return super().__getitem__(key)


class StramFSM:
    def __init__(self):
        self.state = 'group'
        self.group_depth = 0
        self.score = 0
        self.garbage_count = 0

        def group_leave():
            self.group_depth -= 1

        def group_enter():
            self.group_depth += 1
            self.score += self.group_depth

        def garbage_encounter():
            self.garbage_count += 1

        self.transition_table = {
            'garbage': ActionDict(lambda: 'garbage', {
                '!': 'garbage_ignore_next',
                '>': 'group'
            }, actions=defaultdict(lambda: garbage_encounter, {  # Part 2 ugliness
                '!': lambda: None,
                '>': lambda: None,
            })),
            'garbage_ignore_next': defaultdict(lambda: 'garbage'),
            'group': ActionDict(lambda: 'group', dictionary={
                '!': 'group_ignore_next',
                '<': 'garbage'
            }, actions={
                '}': group_leave,
                '{': group_enter
            }),
            'group_ignore_next': defaultdict(lambda: 'group'),
        }

    def symbol(self, symbol):
        self.state = self.transition_table[self.state][symbol]


def process_stream(stream: str):
    fsm = StramFSM()

    for symbol in stream:
        fsm.symbol(symbol)

    return FSMResult(fsm.score, fsm.garbage_count)


if __name__ == '__main__':
    if __name__ == '__main__':
        file_name = 'input' if len(sys.argv) < 2 else sys.argv[1]

        with open(file_name) as file:
            print(process_stream(file.read()))
