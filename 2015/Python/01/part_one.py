"""
Advent of Code 2015 day 01 part one
"""

import sys

INPUT_FILE = "../inputs/01-input.txt"

if __name__ == '__main__':
    floor = 0
    index = 0
    directions = {'(': 1, ')': -1}

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            while True:
                inst = file.read(1)
                if not inst:
                    break # EOF
                if inst[0] in directions:
                    floor += directions[inst[0]]
                else:
                    sys.stderr.write(f"Invalid character found at position '{index+1}'\n")
                    sys.exit(1)
                index += 1
    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"The right floor is '{floor}'")
