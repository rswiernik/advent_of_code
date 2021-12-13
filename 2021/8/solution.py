import sys
from dataclasses import dataclass
from operator import concat
from functools import reduce
from typing import Any, List, Optional, Tuple


numbers = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

uniq = [1, 4, 7, 8]


@dataclass
class Patterns:
    input: List[str]
    output: List[str]

    def all(self):
        return reduce(concat, [self.input, self.output])


class ScrambledDisplay(object):
    def __init__(self, patterns: List[Patterns]):
        self.patterns = patterns

    @staticmethod
    def _is_uniq(pattern: str) -> bool:
        for digit in uniq:
            if len(pattern) == len(numbers[digit]):
                return True
        return False

    def find_simple(self):
        num_simple = 0
        for pattern in self.patterns:
            for item in pattern.output:
                if self._is_uniq(item):
                    num_simple += 1

        return num_simple



if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                items = line.split('|')
                input.append(
                    Patterns(
                        input=items[0].strip().split(' '),
                        output=items[1].strip().split(' ')
                    )
                )

    # Part 1
    display = ScrambledDisplay(input)
    print(display.find_simple())
