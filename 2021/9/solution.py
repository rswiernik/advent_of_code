import sys
from dataclasses import dataclass
from typing import List


Map = List[List[int]]

@dataclass
class Point:
    x: int
    y: int


class Heightmap(object):
    def __init__(self, map: Map):
        self._map = map

    def get(self, point: Point) -> int:
        return self._map[point.x][point.y]

    def _get_neighbors(self, point: Point) -> List[Point]:
        neighbors = []
        for x, y in [
                (-1, 0),
                ( 1, 0),
                ( 0,-1),
                ( 0, 1)]:
            try:
                if any([i < 0 for i in [point.x+x, point.y+y]]) or \
                    any(i >= l for i, l in [
                        (point.x+x, len(self._map)),
                        (point.y+y, len(self._map[point.x]))
                    ]):
                        raise IndexError
                neighbors.append(
                    Point(x=point.x+x, y=point.y+y)
                )
            except IndexError:
                pass

        return neighbors

    def find_low_points(self):
        low_points = []
        for row in range(len(self._map)):
            for col in range(len(self._map[row])):
                point = Point(row, col)
                item = self.get(point)
                neighbors = self._get_neighbors(point)
                comparison = [item < self.get(neighbor) for neighbor in neighbors]
                if all(comparison):
                    low_points.append(item)
        return low_points

    def find_basin(self, point: Point) -> List[Point]:
        self._get_neighbors(point)
        pass

    def calculate_risk(self, low_points: List[int]) -> List[int]:
        return [x+1 for x in low_points]



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

    heightmap = Heightmap(input)
    low_points = heightmap.find_low_points()
    risk_levels = heightmap.calculate_risk(low_points)
    print(sum(risk_levels))



