'''
Advent of Code 2022 - Day 3 Part 1

by @hackermonke
'''
def p1():
    pri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    with open("d3_in.txt", "r") as FILE:
        sacks = FILE.read().splitlines()
        for sack in sacks:
            a = sack[:len(sack)//2]
            b = sack[len(sack)//2:]
            
            # check if string share characters
            for i in a:
                if i in b:
                    sum += pri.index(i) + 1
                    break

    print(sum)

def p2():
    pri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum = 0
    with open("d3_in.txt", "r") as FILE:
        sacks = FILE.read().splitlines()
        for i in range(2, len(sacks), 3):
            a = sacks[i-2]
            b = sacks[i-1]
            c = sacks[i]

            # find intersection of 3 sets
            set_a = set(a)
            set_b = set(b)
            set_C = set(c)

            inter = set_a.intersection(set_b, set_C)
            sum += pri.index(list(inter)[0]) + 1

    print(sum)
    

if __name__ == "__main__":
    p1()
    p2()

