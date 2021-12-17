"""
Advent of Code 2015 day 03 part one
"""

import sys

INPUT_FILE = "../inputs/03-input.txt"

if __name__ == '__main__':
    cur_pos = [0, 0]
    path = [[0, 0]]
    directions = {
        'v': [0, -1],
        '>': [1, 0],
        '^': [0, 1],
        '<': [-1, 0]
    }

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            line = file.readline()
            for index, direction in enumerate(line):
                if direction in directions:
                    cur_pos = [sum(x) for x in zip(cur_pos, directions[direction])]
                else:
                    sys.stderr.write(f"Invalid character found at position '{index+1}'\n")
                    sys.exit(1)

                if cur_pos not in path:
                    path.append(cur_pos.copy())
    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"At least {len(path)} houses received one present")
    sys.exit(0)
