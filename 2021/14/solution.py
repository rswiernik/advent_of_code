import sys
from collections import defaultdict
from typing import List


def polymerize(input: List[str], steps: int):
    output = [x for x in input]
    for step in range(0, steps):
        next = []
        for pos in range(len(output)):
            current = output[pos]

            if pos-1 < 0:
                next.append(current)
                pos += 1
                continue

            last = output[pos-1]

            rule = rules.get(''.join([last, current]), None)
            if rule:
                next.append(rule)
                pos += 1
            next.append(current)

        output = next
    return output


if __name__ == "__main__":
    in_file = sys.argv[1]

    input = ""
    rules = {}
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                if not input:
                    input = line.strip()
                else:
                    (pattern, x) = line.strip().split(' -> ')
                    rules[pattern] = x

    input = [x for x in input]
    print(input)
    print(rules)
    print('-----------------')

    # Part 1
    # output = polymerize(input, 10)

    # Part 2
    output = polymerize(input, 40)
    print(len(output))

    items = defaultdict(lambda: 0)
    for i in output:
        items[i] += 1

    max = None
    min = None
    for item, n in items.items():
        if not max or n > max:
            max = n
        elif not min or n < min:
            min = n

    print(max-min)



