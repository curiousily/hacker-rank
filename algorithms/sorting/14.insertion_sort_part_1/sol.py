import sys
file = open('in.txt')
sys.stdin = file


def print_seq(seq):
    print(' '.join('{}'.format(v) for v in seq))

S = int(input())
ar = [int(x) for x in input().split()]

v = ar[S - 1]

i = S - 2

while ar[i] > v and i >= 0:
    ar[i + 1] = ar[i]
    i -= 1
    print_seq(ar)

ar[i + 1] = v
print_seq(ar)
