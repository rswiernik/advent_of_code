import math
import sys
from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point

    @staticmethod
    def _distance(a: Point, b: Point) -> float:
        return math.sqrt(
            ( abs(a.x - b.x) )**2 + \
            ( abs(a.y - b.y) )**2
        )


    def on_line(self) -> List[Point]:
        def xy_range(a, b):
            direction = -1 if a - b > 0 else 1
            b += direction
            print('{} -> {} | {}'.format(a,b,direction))
            return range(a, b, direction)

        points = []

        if self.start.x == self.end.x:
            static = self.start.x
            dynamic = (self.start.y, self.end.y)
            func = lambda a,b: (a,b)
        elif self.start.y == self.end.y:
            static = self.start.y
            dynamic = (self.start.x, self.end.x)
            func = lambda a,b: (b,a)
        else:
            raise Exception('We cant do diagonals!')

        for val in xy_range(dynamic[0], dynamic[1]):
            row, col = func(val, static)
            print("{},{}".format(row, col))
            points.append(Point(row, col))

        length = len(points)
        diff = abs(dynamic[0]-dynamic[1])+1
        assert length == diff, '{} != {}'.format(length, diff)
        return points



class VentMap(object):
    def __init__(self, lines: List[Line]):
        self.lines = lines
        # Initialize map with line bounding box
        max_x = 0
        max_y = 0
        for line in self.lines:
            for point in [line.start, line.end]:
                if point.x > max_x:
                    max_x = point.x
                if point.y > max_y:
                    max_y = point.y
        self.map = [
            [ 0 for _ in range(max_y+1)] for x in range(max_x+1)
        ]

    def calculate_vents(self) -> int:
        # Populate the map with line info
        poi = 0
        for line in self.lines:
            if not (line.start.x == line.end.x or \
                    line.start.y == line.end.y):
                continue
            print('>>> {}'.format(line))

            # Get points on the line
            points = line.on_line()
            print(points)

            # Add them to the map
            for point in points:
                self.map[point.x][point.y] += 1
                if self.map[point.x][point.y] == 2:
                    poi += 1

        print('\n'.join(
            [str([str(n) if n != 0 else '.' for n in x]) for x in self.map]
        ))
        return poi



if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for l in f.readlines():
            if l and l != '\n':
                partial = l.strip().split(' -> ')
                start = partial[0].split(',')
                end = partial[1].split(',')
                input.append(
                    Line(
                        start=Point(int(start[0]), int(start[1])),
                        end=Point(int(end[0]), int(end[1])),
                    )
                )
    vent_map = VentMap(input)
    print(vent_map.calculate_vents())
