import sys
from typing import List


Map = List[List[int]]

class Heightmap(object):
    def __init__(self, map: Map):
        self.map = map

    def _get_neighbors(self, row, col):
        neighbors = []
        for x, y in [
                (-1, 0),
                ( 1, 0),
                ( 0,-1),
                ( 0, 1)]:
            try:
                if any([i < 0 for i in [row+x, col+y]]):
                    raise IndexError
                neighbors.append(
                    self.map[row+x][col+y]
                )
            except IndexError:
                pass

        return neighbors

    def find_low_points(self):
        low_points = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                item = self.map[row][col]
                neighbors = self._get_neighbors(row, col)
                comparison = [item < neighbor for neighbor in neighbors]
                if all(comparison):
                    low_points.append(item)
        return low_points

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



