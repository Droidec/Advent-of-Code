"""
Advent of Code 2015 day 04 part two
"""

import hashlib

if __name__ == '__main__':
    key = 'bgvyzdsv'
    value = 1
    while True:
        seed = key + str(value)
        md5_hash = hashlib.md5(seed.encode()).hexdigest()
        if md5_hash.startswith('000000'):
            break
        value += 1

    print(f"The answer is '{value}'")
