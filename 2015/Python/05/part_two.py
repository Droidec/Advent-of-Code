"""
Advent of Code 2015 day 05 part two
"""

import re
import sys

INPUT_FILE = "../inputs/05-input.txt"

if __name__ == '__main__':
    nice_count = 0

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            for line in file:
                # Pair of any two letters that appears at least
                # twice in the string without overlapping (Property 1)
                twice = re.findall(r'(.)\1{1,}', line)

                nice_count += 1

    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"There are '{nice_count}' nice strings")
