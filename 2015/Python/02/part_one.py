"""
Advent of Code 2015 day 02 part one
"""

import sys

INPUT_FILE = "../inputs/02-input.txt"

def calculate_surface_area(l=0, w=0, h=0):
    return 2*l*w + 2*w*h + 2*h*l

if __name__ == '__main__':
    total = 0

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            while True:
                box_dim = file.readline();
                if not box_dim:
                    break # EOF

                list_dim = box_dim.split('x')
                l = int(list_dim[0])
                w = int(list_dim[1])
                h = int(list_dim[2])

                total += calculate_surface_area(l, w, h);
                total += min(min(l*h, h*w), l*w)

    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"They should order '{total}' square feet in total")
