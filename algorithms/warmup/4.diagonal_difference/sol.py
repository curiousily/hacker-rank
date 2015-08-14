import sys
file = open('in.txt')
sys.stdin = file

n = int(input())
di_1 = 0
di_2 = n - 1
d1 = 0
d2 = 0
for i in range(n):
    row = [int(x) for x in input().split()]
    d1 += row[di_1]
    di_1 += 1
    d2 += row[di_2]
    di_2 -= 1
print(abs(d1-d2))
