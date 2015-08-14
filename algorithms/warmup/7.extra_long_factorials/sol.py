import sys
file = open('in.txt')
sys.stdin = file

import math
n = int(input())
print(math.factorial(n))
