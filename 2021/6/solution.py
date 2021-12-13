import sys
from typing import Any, List, Optional
from collections import defaultdict



# Part 1
class School(object):
    def __init__(self, input):
        self.school = []
        for age in input:
            self.school.append(age)

    @staticmethod
    def _tick(age: int) -> (int, bool):
        if age == 0:
            return (6, True)
        else:
            return ((age - 1), False)

    def simulate(self, days: int):
        for day in range(days):
            if (day % 10 == 0):
                print('{} : {}'.format(day,len(self.school)))
            to_add = 0
            for x in range(len(self.school)):
                (new_age, create_child) = self._tick(self.school[x])
                self.school[x] = new_age
                if create_child:
                    to_add += 1
            self.school.extend([8] * to_add)

# Part 2
class NewSchool(object):
    def __init__(self, input):
        self.school = defaultdict(lambda: 0)
        for age in input:
            self.school[age] += 1

    def simulate(self, days: int):
        for day in range(days):
            if (day % 10 == 0):
                print('{} : {}'.format(day, sum(self.school.values())))
            to_add = 0


            next_school = defaultdict(lambda: 0)
            for x in range(0, 8):
                if x == 0:
                    next_school[6] += self.school[x]
                    next_school[8] = next_school[6]

                next_school[x] += self.school[x+1]
            self.school = next_school
        print('{} : {}'.format(days, sum(self.school.values())))

if __name__ == "__main__":
    in_file = sys.argv[1]

    input = []
    with open(in_file) as f:
        for line in f.readlines():
            if line and line != '\n':
                input.extend([int(x) for x in line.strip().split(',')])

    # Part 1
    school = School(input)
    school.simulate(80)
    print(len(school.school))

    # Part 2
    school = NewSchool(input)
    school.simulate(256)
