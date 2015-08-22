import sys
file = open('in.txt')
sys.stdin = file

_ = input()
sticks = sorted([int(x) for x in input().split()])
while sticks:
    print(len(sticks))
    min_stick = sticks[0]
    sticks = [stick - min_stick for stick in sticks if stick - min_stick > 0]
