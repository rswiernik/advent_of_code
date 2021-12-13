import sys
from dataclasses import dataclass
from typing import List, Optional


char_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

symbol_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

symbols = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
}

def check_syntax(line: str) -> (Optional[str], List[str]):
    stack = []
    # Part 1
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
                return symbol, []

    # Part 2
    if len(stack) != 0:
        # Incomplete!
        ending = []
        for item in stack[::-1]:
            ending.append(symbols[item])
    return None, ending



def score_chars(chars: List[str]) -> int:
    total = 0
    for char in chars:
        total += char_score[char]
    return total


def score_endings(endings: List[str]) -> int:
    scores = []
    for ending in endings:
        total = 0
        for char in ending:
            total = total * 5
            total += symbol_score[char]
        scores.append(total)
    return scores


if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                input.append(line.strip())
    # Part 1
    illegal_chars = []
    endings = []
    for line in input:
        c, ending = check_syntax(line)
        if c:
            illegal_chars.append(c)
        elif ending:
            endings.append(ending)

    # part 1
    print(illegal_chars)
    print('illegal characters score: {}'.format(score_chars(illegal_chars)))

    # part 2
    # print(endings)
    ending_scores = score_endings(endings)
    print('Winner: {}'.format(sorted(ending_scores)[int(len(ending_scores)/2)]))
