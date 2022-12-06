'''
Advent of Code 2022 - Day 6 Part 2

by @hackermonke
'''

with open('d6_in.txt') as f:
    data = f.read()
    for i in range(0, len(data)):
        if i + 14 > len(data):
            break

        buffer = data[i:i+14]
        if len(set(buffer)) == 14:
            print(buffer, i+14)
            break
        