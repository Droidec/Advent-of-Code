"""
Advent of Code 2015 day 02 part one
"""

import sys

INPUT_FILE = "../inputs/02-input.txt"

if __name__ == '__main__':
    total = 0

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            for line in file:
                l, w, h = line.split('x')
                l, w, h = int(l), int(w), int(h)
                s1 = l * w
                s2 = l * h
                s3 = w * h
                extra = min(s1, s2, s3)
                total += 2*s1 + 2*s2 + 2*s3 + extra
    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"They should order '{total}' square feet in total")
