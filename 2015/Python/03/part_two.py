"""
Advent of Code 2015 day 03 part two
"""

import sys

INPUT_FILE = "../inputs/03-input.txt"

if __name__ == '__main__':
    santa_pos = [0, 0]
    robo_santa_pos = [0, 0]
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
                    if index % 2 == 0:
                        # Move santa
                        santa_pos = [sum(x) for x in zip(santa_pos, directions[direction])]
                        if santa_pos not in path:
                            path.append(santa_pos.copy())
                    else:
                        # Move robo-santa
                        robo_santa_pos = [sum(x) for x in zip(robo_santa_pos, directions[direction])]
                        if robo_santa_pos not in path:
                            path.append(robo_santa_pos.copy())
                else:
                    sys.stderr.write(f"Invalid character found at position '{index+1}'\n")
                    sys.exit(1)
    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"At least '{len(path)}' houses received one present")
    sys.exit(0)
