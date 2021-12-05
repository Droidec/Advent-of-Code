"""
Advent of Code 2015 day 02 part two
"""

import sys

INPUT_FILE = "../inputs/02-input.txt"

if __name__ == '__main__':
    total = 0

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            for line in file:
                dims = line.split('x')
                dims = sorted([int(dim) for dim in dims])
                total += dims[0]*2 + dims[1]*2
                total += dims[0]*dims[1]*dims[2]
    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"They should order '{total}' feet of ribbon in total")
