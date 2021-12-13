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


    @staticmethod
    def _next(a: Point, b: Point) -> Point:
        directions = {
            'x': 0,
            'y': 0,
        }
        for axis in ['x', 'y']:
            if getattr(a, axis) - getattr(b, axis) > 0:
                directions[axis] = -1
            elif getattr(a, axis) - getattr(b, axis) < 0:
                directions[axis] = 1
        new_point = Point(
            x = a.x + directions['x'],
            y = a.y + directions['y']
        )
        # print('{} -> {} | {}'.format(a,b,new_point))
        return new_point


    def on_line(self) -> List[Point]:
        points = []
        cursor = Point(self.start.x, self.start.y)
        while cursor != self.end:
            points.append(cursor)
            cursor = self._next(cursor, self.end)

        points.append(self.end)
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

    def calculate_vents(self, diagonals: bool) -> int:
        # Populate the map with line info
        poi = 0
        for line in self.lines:
            if not diagonals and \
                    not (line.start.x == line.end.x or \
                    line.start.y == line.end.y):
                continue
            #print('>>> {}'.format(line))

            # Get points on the line
            points = line.on_line()
            #print(points)

            # Add them to the map
            for point in points:
                self.map[point.x][point.y] += 1
                if self.map[point.x][point.y] == 2:
                    poi += 1

        #print('\n'.join(
        #    [str([str(n) if n != 0 else '.' for n in x]) for x in self.map]
        #))
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
    print(vent_map.calculate_vents(diagonals=False))

    vent_map = VentMap(input)
    print(vent_map.calculate_vents(diagonals=True))
