import sys
import math
from typing import Any, List, Optional
from collections import defaultdict


class CrabGang(object):
    def __init__(self, positions: List[int], linear: bool):
        self.linear = linear
        self.positions = defaultdict(lambda: 0)
        for pos in positions:
            self.positions[pos] += 1

    def cost(self, val):
        if self.linear:
            return val
        else:
            return math.floor(((val * val) + val)/2)

    def align(self):
        cost = defaultdict(lambda: 0)
        for dest in range(max(self.positions.keys())):
            for position, num_crabs in self.positions.items():
                cost[dest] += self.cost(abs(position-dest)) * num_crabs

        return min(cost.values())

if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                input.extend([int(x) for x in line.strip().split(',')])

    # Part 1
    gang = CrabGang(input, linear=True)
    print(gang.align())

    # Part 2
    gang = CrabGang(input, linear=False)
    print(gang.align())
