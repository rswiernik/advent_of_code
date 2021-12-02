import sys
from typing import List

def find_increased(input: List) -> int:
    depth_increased = 0

    current_count = None
    previous_count = None

    for current_count in input:
        if previous_count and \
            current_count > previous_count:
                depth_increased += 1
        previous_count = current_count

    return depth_increased

def find_increased_sliding_window(input: List) -> int:
    depth_increased = 0
    window = []
    for count in input:
        window.append(count)
        if len(window) < 4:
            continue
        elif len(window) == 5:
            window.pop(0)

        a_sum = sum(window[:-1])  # First Window (AAA)
        b_sum = sum(window[1:])  # Second Window (BBB)


        if b_sum > a_sum:
            depth_increased += 1

    return depth_increased


if __name__ == "__main__":
    in_file = sys.argv[1]
    with open(in_file) as f:
        input = f.readlines()

    input_array = []
    for line in input:
        if line:
            entry = int(str(line.strip()))
            input_array.append(entry)

    num_increased = find_increased(input_array)
    print(num_increased)

    num_increased = find_increased_sliding_window(input_array)
    print(num_increased)
