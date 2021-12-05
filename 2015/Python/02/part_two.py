"""
Advent of Code 2015 day 02 part two
"""

import sys

INPUT_FILE = "../inputs/02-input.txt"

if __name__ == '__main__':
    total = 0

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            while True:
                box_dim = file.readline();
                if not box_dim:
                    break # EOF

                list_dim = box_dim.split('x')
                list_dim = [int(dim) for dim in list_dim]
                list_dim = sorted(list_dim)
                total += list_dim[0]*2 + list_dim[1]*2
                total += list_dim[0]*list_dim[1]*list_dim[2]

    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"They should order '{total}' feet of ribbon in total")
