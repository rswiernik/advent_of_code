import sys
from dataclasses import dataclass
from operator import concat
from functools import reduce
from typing import Any, Dict, List, Optional


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
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


class Signal:
    def __init__(self, input: List[str], output: List[str]):
        self.input = [''.join(sorted(x)) for x in input]
        self.output = [''.join(sorted(x)) for x in output]

    def decode(self):
        print('{} | {}'.format(self.input, self.output))
        possible = {}

        for pattern in self.input:
            match = self.is_uniq(pattern)
            if match:
                possible[match] = pattern

        def a_in_b(a, b):
            return all([(x in b) for x in a])

        stack = [x for x in self.input]
        while len(stack) > 0:
            pattern = stack.pop()
            if pattern in possible.values():
                print(pattern)
                print(possible)
                continue

            # WARNING JUMBLE AHEAD
            length = len(pattern)
            if length == 6:
                if a_in_b(possible[4], pattern):
                    possible[9] = pattern
                elif a_in_b(possible[1], pattern) or \
                        a_in_b(possible[7], pattern):
                    possible[0] = pattern
                else:
                    possible[6] = pattern
                continue
            elif length == 5:
                if a_in_b(possible[1], pattern):
                    possible[3] = pattern
                    continue
                elif six := possible.get(6):
                    if a_in_b(pattern, six):
                        possible[5] = pattern
                    else:
                        possible[2] = pattern
                    continue
            # Shove this at the beginning of the stack
            stack.insert(0, pattern)

        key = {
            val: key for (key, val) in possible.items()
        }
        print('\n'.join(['{}: {}'.format(key, val) for (key, val) in key.items()]))
        print('---------------')
        out = []
        for pattern in self.output:
            out.append(key[pattern])
        assert len(out) == 4
        num = int(''.join([str(x) for x in out]))
        return num


    @staticmethod
    def is_uniq(pattern: str) -> Optional[int]:
        for digit in uniq:
            if len(pattern) == len(numbers[digit]):
                return digit
        return None


class ScrambledDisplay(object):
    def __init__(self, patterns: List[Signal]):
        self.patterns = patterns


    def find_simple(self):
        num_simple = 0
        for pattern in self.patterns:
            for item in pattern.output:
                if Signal.is_uniq(item):
                    num_simple += 1
        return num_simple

    def search(self):
        results = {}
        for pattern in self.patterns:
            results[' '.join(pattern.output)] = pattern.decode()
        print(results)
        print(sum(results.values()))


if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                items = line.split('|')
                input.append(
                    Signal(
                        input=items[0].strip().split(' '),
                        output=items[1].strip().split(' ')
                    )
                )


    # Part 1
    display = ScrambledDisplay(input)
    print(display.find_simple())
    print()


    # Part 2
    display = ScrambledDisplay(input)
    display.search()
