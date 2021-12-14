import sys
from dataclasses import dataclass
from typing import List


@dataclass
class Octopus:
    x: int
    y: int
    value: int
    flashed: bool = False

    def __eq__(self, other):
        if self.x == other.x and \
                self.y == other.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

Map = List[List[Octopus]]


class OctopusMap(object):
    def __init__(self, map: Map):
        self._map = map
        self.flashes = 0

    def _get(self, x, y) -> Octopus:
        return self._map[x][y]

    def _get_neighbors(self, octopus: Octopus) -> List[Octopus]:
        neighbors = []
        for x, y in [
                (-1, 0),
                ( 1, 0),
                ( 1, 1),
                (-1, 1),
                ( 1, -1),
                (-1, -1),
                ( 0,-1),
                ( 0, 1)]:
            try:
                if any([i < 0 for i in [octopus.x+x, octopus.y+y]]) or \
                    any(i >= l for i, l in [
                        (octopus.x+x, len(self._map)),
                        (octopus.y+y, len(self._map[octopus.x]))
                    ]):
                        raise IndexError
                neighbors.append(
                    self._get(x=octopus.x+x, y=octopus.y+y)
                )
            except IndexError:
                pass

        return neighbors

    def step(self):
        # Increase by 1
        for row in self._map:
            for octopus in row:
                octopus.value += 1
        for row in self._map:
            for octopus in row:
                if not octopus.flashed:
                    self.check_flash(octopus)

        # Reset flashes
        for row in self._map:
            for octopus in row:
                octopus.flashed = False


    def check_flash(self, octopus: Octopus, chained: bool = False):
        if not octopus.flashed:
            if chained:
                octopus.value += 1

            if octopus.value > 9:
                self.flashes += 1
                octopus.flashed = True
                octopus.value = 0
                for neighbor in self._get_neighbors(octopus):
                    if not neighbor.flashed:
                        self.check_flash(neighbor, chained=True)


if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                row = []
                for x in line.strip():
                    row.append(int(x))
                input.append(row)

    # Part 1
    o_map = OctopusMap(
        [[Octopus(row, col, input[row][col]) for col in range(len(input[row]))]
         for row in range(len(input))]
    )
    for x in range(1, 101):
        o_map.step()
        if x % 10 == 0:
            print('step: {}'.format(x))
            print('\n'.join([''.join([str(n.value) for n in x]) for x in o_map._map]))
            print('--------------')

    print('Observed flashes: {}'.format(o_map.flashes))
