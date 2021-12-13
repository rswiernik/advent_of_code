import sys
from dataclasses import dataclass
from typing import List


score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

symbols = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
}

def check_syntax(line: str) -> str:
    stack = []
    for symbol in line:
        if symbol in symbols.keys():
            stack.append(symbol)
        elif symbol in symbols.values():
            last = stack.pop()
            expected = symbols[last]
            if symbol != expected:
                print('Expected {}, but found {} instead'.format(
                    expected,
                    symbol
                ))
                return symbol

def score_chars(chars: List[str]) -> int:
    total = 0
    for char in chars:
        total += score[char]
    return total


if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                input.append(line.strip())
    # Part 1
    illegal_chars = []
    for line in input:
        c = check_syntax(line)
        if c:
            illegal_chars.append(c)

    print(illegal_chars)
    print(score_chars(illegal_chars))
