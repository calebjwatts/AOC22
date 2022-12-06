'''
Advent of Code 2022 - Day 4 Part 1

by @hackermonke
'''
import re

with open('d4_in.txt') as f:
    pairs = f.read().splitlines()
    count = 0

    for pair in pairs:
        ranges = list(map(int, re.findall(r'[0-9]{1,2}', pair)))
        if (ranges[0] >= ranges[2] and ranges[1] <= ranges[3]) or (ranges[2] >= ranges[0] and ranges[3] <= ranges[1]):
            count += 1
    print(count)
