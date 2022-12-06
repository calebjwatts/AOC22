'''
Advent of Code 2022 - Day 2 Part 2

by @hackermonke

Elf plays
A: Rock 1
B: Paper 2
C: Scissors 3

I need to
X: lose 0
Y: draw 3
Z: win 6
'''

points = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6
}

with open("d2_in.txt", "r") as FILE:
    rounds = FILE.read().splitlines()
    score = 0
    for round in rounds:
        score += points[round]

print(score)
