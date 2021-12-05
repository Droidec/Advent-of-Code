"""
Advent of Code 2015 day 01 part two
"""

import sys

INPUT_FILE = "../inputs/01-input.txt"

if __name__ == '__main__':
    floor = 0
    index = 0
    direction = {'(': 1, ')': -1}

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            while True:
                inst = file.read(1)
                if not inst:
                    break # EOF
                if inst[0] in direction:
                    floor += direction[inst[0]]
                else:
                    sys.stderr.write(f"Invalid character found at position '{index+1}'\n")
                    sys.exit(1)
                if floor == -1:
                    print(f"Basement is reached at position '{index+1}'")
                    sys.exit(0)
                index += 1
    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    sys.stderr.write("The basement was never reached?\n")
    sys.exit(1)
