import sys
from typing import List

def find_increased(input: List) -> int:
    years_increased = 0

    current_count = None
    previous_count = None

    for current_count in input:
        if previous_count and \
            current_count > previous_count:
                years_increased += 1
        previous_count = current_count

    return years_increased

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

