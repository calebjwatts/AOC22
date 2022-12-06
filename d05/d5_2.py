'''
Advent of Code 2022 - Day 5 Part 2

by @hackermonke
'''
from parse import *

with open('d5_in.txt') as f:
    lines = f.read().splitlines()[10:]
    stacks = [
        ["D", "B", "J", "V"],
        ["P", "V", "B", "W", "R", "D", "F"],
        ["R", "G", "F", "L", "D", "C", "W", "Q"],
        ["W", "J", "P", "M", "L", "N", "D", "B"],
        ["H", "N", "B", "P", "C", "S", "Q"],
        ["R", "D", "B", "S", "N", "G"],
        ["Z", "B", "P", "M", "Q", "F", "S", "H"],
        ["W", "L", "F"],
        ["S", "V", "F", "M", "R"]
    ]
    for line in lines:
        n, f, t = parse('move {:d} from {:d} to {:d}', line)
        moving = []
        for i in range(0, n):
            moving.append(stacks[f - 1].pop())
        stacks[t-1].extend(reversed(moving))

    print([stacks[i][-1] for i in range(0, 9)])
    