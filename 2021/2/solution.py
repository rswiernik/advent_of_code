import sys
from typing import List

def move_ship(instructions: List) -> (int, int):
    x = 0
    y = 0
    for command, amount in instructions:
        if command == 'forward':
            x += amount
        elif command == 'up':
            y = y - amount
        elif command == 'down':
            y += amount

    return (x, y)

def move_ship_with_aim(instructions: List) -> (int, int):
    x = 0
    depth = 0
    aim = 0
    for command, amount in instructions:
        if command == 'forward':
            x += amount
            depth = depth + (aim * amount)
        elif command == 'up':
            aim = aim - amount
        elif command == 'down':
            aim += amount

    return (x, depth)

if __name__ == "__main__":
    in_file = sys.argv[1]
    with open(in_file) as f:
        input = f.readlines()

    input_array = []
    for line in input:
        if line:
            entry = str(line.strip()).split(' ')
            entry[1] = int(entry[1])
            input_array.append(tuple(entry))

    x, y  = move_ship(input_array)
    print((x,y))
    print(x * y)

    x, y  = move_ship_with_aim(input_array)
    print((x,y))
    print(x * y)

