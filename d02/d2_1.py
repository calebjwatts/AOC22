'''
Advent of Code 2022 - Day 2 Part 2

by @hackermonke

Elf plays
A: Rock 1
B: Paper 2
C: Scissors 3

I play
X: Rock 1
Y: Paper 2
Z: Scissors 3
'''

points = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3
}

with open("d2_in.txt", "r") as FILE:
    rounds = FILE.read().splitlines()
    score = 0
    for round in rounds:
        score += points[round]

print(score)
