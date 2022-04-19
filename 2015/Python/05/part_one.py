"""
Advent of Code 2015 day 05 part one
"""

import re
import sys

INPUT_FILE = "../inputs/05-input.txt"

if __name__ == '__main__':
    nice_count = 0

    try:
        with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
            for line in file:
                # At least three vowels (Property 1)
                vowels = re.findall(r'[aeiou]', line, re.IGNORECASE)
                if len(vowels) < 3:
                    continue

                # Letter appears twice in a row (Property 2)
                if not re.search(r'(.)\1{1,}', line):
                    continue

                # Does not countain substrings (Property 3)
                if any(substring in line for substring in ('ab', 'cd', 'pq', 'xy')):
                    continue

                nice_count += 1

    except IOError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    print(f"There are '{nice_count}' nice strings")
