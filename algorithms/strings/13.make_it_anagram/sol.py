import sys
file = open('in.txt')
sys.stdin = file

from collections import defaultdict
from functools import reduce

str_1 = input()
str_2 = input()

diff = defaultdict(int)

for ch in str_1:
    diff[ch] += 1

for ch in str_2:
    diff[ch] -= 1

deletions = reduce(lambda x, y: x + abs(y), diff.values(), 0)

print(deletions)
