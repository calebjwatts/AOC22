'''
Advent of Code 2022 - Day 1 Part 1

by @hackermonke
'''

with open("one_in.txt", "r") as FILE:
    lines = FILE.readlines()

    totals = [0]
    i = 0
    for line in lines:
        if line != '\n':
            totals[i] += int(line)
        else:
            i += 1
            totals.append(0)

print(totals)

print(max(totals))

    
