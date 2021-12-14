import math
import sys
from dataclasses import dataclass
from typing import List

@dataclass
class Point:
    x: int
    y: int


@dataclass
class Fold:
    axis: str  # 'x' or 'y'
    n: int  # line where the fold needs to happen


class ThermalMap(object):
    def __init__(self, points: List[Point]):
        self.points = points
        self.x_max = 0
        self.y_max = 0
        for point in self.points:
            if point.x > self.x_max:
                self.x_max = point.x
            if point.y > self.y_max:
                self.y_max = point.y

    def fold(self, fold: Fold):
        if fold.axis == 'x':
            y_fold = self.y_max
            x_fold = fold.n
            self.x_max = x_fold-1
        elif fold.axis == 'y':
            y_fold = fold.n
            x_fold = self.x_max
            self.y_max = y_fold-1

        new_points = []
        for point in self.points:
            x_diff = point.x - x_fold
            y_diff = point.y - y_fold
            if x_diff > 0 :
                new_points.append(
                    Point((x_fold-x_diff), point.y)
                )
            elif y_diff > 0 :
                new_points.append(
                    Point(point.x, (y_fold-y_diff))
                )
            else:
                new_points.append(point)

        self.points = new_points

    def get_visible(self):
        out = []
        for col in range(self.y_max + 1):
            out.append(['.' for x in range(self.x_max + 1)])


        visible = 0
        for point in self.points:
            if out[point.y][point.x] != '#':
                visible += 1
                out[point.y][point.x] = '#'
        print('\n'.join([''.join(x) for x in out]))
        return visible


if __name__ == "__main__":
    in_file = sys.argv[1]

    points = []
    folds = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                if 'fold along ' in line:
                    line = line.strip().replace('fold along ', '')
                    (axis, n) = line.split('=')
                    folds.append(Fold(axis, int(n)))
                else:
                    (x, y) = line.strip().split(',')
                    points.append(Point(int(x), int(y)))

    # Part 1
    t_map = ThermalMap(points)
    print('---------------')
    print('Visible: {}'.format(t_map.get_visible()))
    for fold in folds:
        t_map.fold(fold)
        print('---------------')
        print('Visible: {}'.format(t_map.get_visible()))
        break

