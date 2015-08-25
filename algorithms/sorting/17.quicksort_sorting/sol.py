import sys
file = open('in.txt')
sys.stdin = file


def print_seq(seq):
    print(' '.join('{}'.format(v) for v in seq))


def partition(seq, p):
    l = []
    r = []

    for a in seq:
        if a > p:
            r.append(a)
        else:
            l.append(a)
    return (l, r)


def quicksort(seq):
    if not seq or len(seq) == 1:
        return seq
    p = seq[0]
    seq.remove(p)
    l, r = partition(seq, p)
    left = quicksort(l)
    right = quicksort(r)
    result = left + [p] + right
    print_seq(result)
    return result

_ = input()
A = [int(x) for x in input().split()]

quicksort(A)
