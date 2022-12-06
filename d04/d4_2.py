'''
Advent of Code 2022 - Day 4 Part 2

by @hackermonke
'''
import re

with open('d4_in.txt') as f:
    pairs = f.read().splitlines()
    count = 0

    for pair in pairs:
        ranges = list(map(int, re.findall(r'[0-9]{1,2}', pair)))
        a = set([i for i in range(ranges[0], ranges[1] + 1)])
        b = set([i for i in range(ranges[2], ranges[3] + 1)])
        if a.intersection(b):
            count += 1
        
    print(count)
