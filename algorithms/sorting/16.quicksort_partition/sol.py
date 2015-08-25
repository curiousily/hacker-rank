import sys
file = open('in.txt')
sys.stdin = file


def print_seq(seq):
    print(' '.join('{}'.format(v) for v in seq))


S = int(input())
A = [int(x) for x in input().split()]

p = A[0]
A.remove(p)

l = []
r = []

for a in A:
    if a > p:
        r.append(a)
    else:
        l.append(a)

print_seq(l + [p] + r)
