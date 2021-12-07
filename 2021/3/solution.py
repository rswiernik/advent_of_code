import sys
from typing import List
from collections import defaultdict


Report = List[List[int]]


def array_to_binary_str(array):
    return ''.join([str(x) for x in array])


# Part 1
# The 'I am very clever' solution that doesn't
# help me in part 2 whatsoever
def evaluate_diagnostics(report: Report) -> (int, int):
    counter = None
    for entry in report:
        if not counter:
            counter = [0] * len(entry)
        for pos in range(0, len(entry)):
            counter[pos] += entry[pos]

    gamma = []
    epsilon = []
    for x in counter:
        if x > (len(report)/2):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    return (gamma, epsilon)


# Part 2
def transpose(input: Report) -> Report:
    return list(map(list, zip(*input)))


def most_common_bit(bit_sequence: List[int], default: int = 0) -> int:
    ones = bit_sequence.count(1)
    zeros = bit_sequence.count(0)
    if ones > zeros:
        return default
    elif ones < zeros:
        return not default
    else:
        return default


def get_part_rating(
        report: Report,
        preferred_bit: int,
        ) -> str:
    column = 0
    while len(report) > 1:
        t = transpose(report)
        criteria  = most_common_bit(t[column], preferred_bit)


        temp_report = []
        row = 0
        for bit in t[column]:
            if bit == criteria:
                temp_report.append(report[row])
            row += 1

        report = temp_report
        column += 1

    return array_to_binary_str(report[0])


def get_oxygen_rating(report: Report) -> str:
    return get_part_rating(report, 1)

def get_co2_rating(report: Report) -> str:
    return get_part_rating(report, 0)



if __name__ == "__main__":
    in_file = sys.argv[1]
    with open(in_file) as f:
        input = f.readlines()

    input_array = []
    for line in input:
        if line:
            input_array.append(
                [int(x) for x in list(line.strip())]
            )

    # Part 1
    gamma, epsilon = evaluate_diagnostics(input_array)

    gamma = int(array_to_binary_str(gamma),2)
    epsilon = int(array_to_binary_str(epsilon),2)
    print('gamma: {}, epsilon: {}'.format(gamma, epsilon))
    print('result: {}'.format(gamma * epsilon))

    # Part 2
    oxygen_rating = int(get_oxygen_rating(input_array), 2)
    print()
    co2_rating = int(get_co2_rating(input_array), 2)
    print('oxygen rating: {}, co2 rating: {}'.format(
        oxygen_rating,
        co2_rating,
    ))
    print('life support rating: {}'.format(
        (oxygen_rating * co2_rating)
    ))
