import sys
from collections import defaultdict
from typing import List


def polymerize(input: List[str], rules, steps: int):
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


def do_the_math(intput):
    items = defaultdict(lambda: 0)
    for i in intput:
        items[i] += 1
    print(dict(items))
    return max(items.values()) - min(items.values())


def inplace_polymerizer(input: List[str], rules, steps: int):
    input = [x for x in input]
    print(input)
    chains = defaultdict(lambda: 0)
    for pos in range(0, len(input)):
        if pos == len(input) - 1:
            chains['{} '.format(input[pos])] += 1
        else:
            chains[''.join([input[pos],input[pos+1]])] += 1

    for step in range(0, steps):
        new_chains = defaultdict(lambda: 0)
        for (key, tally) in chains.items():
            rule = rules.get(key)
            if rule:
                new_chains['{}{}'.format(key[0],rule)] += tally
                new_chains['{}{}'.format(rule,key[1])] += tally
            elif key[1] == ' ':
                new_chains[key] += tally
        chains = new_chains

    letter_count = defaultdict(lambda: 0)
    for (key, val) in chains.items():
        letter_count[key[0]] += val

    print(dict(letter_count))
    return max(letter_count.values()) - min(letter_count.values())


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
    # print(rules)
    print('-----------------')

    # Part 1
    output = polymerize(input, rules, 10)
    print(len(output))
    print(do_the_math(output))


    print('-----------------')
    # print(new_rules)
    print(inplace_polymerizer(input, rules,  40))
