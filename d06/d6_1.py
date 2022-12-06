'''
Advent of Code 2022 - Day 6 Part 1

by @hackermonke
'''

with open('d6_in.txt') as f:
    data = f.read()
    for i in range(0, len(data), 4):
        if i + 4 > len(data):
            break

        buffer = data[i:i+4]
        if len(set(buffer)) == 4:
            print(buffer, i+4)
            break
        