# -*- coding: utf-8 -*-
"""
Advent of Code 2015 day 01 part one
"""

import sys

INPUT_FILE = "../../inputs/01-input.txt"

if __name__ == '__main__':
    floor = 0
    direction = {'(': 1, ')': -1}

    with open(INPUT_FILE, 'r', encoding='UTF-8') as file:
        inst = file.read()
        for index, char in enumerate(inst):
            if char in direction:
                floor += direction[char]
            else:
                sys.stderr.write(f"Invalid character found at position '{index+1}'\n")
                sys.exit(1)

            if floor == -1:
                print(f"Basement is reached at position '{index+1}'")
                break
