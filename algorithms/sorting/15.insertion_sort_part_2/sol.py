import sys
file = open('in.txt')
sys.stdin = file


def print_seq(seq):
    print(' '.join('{}'.format(v) for v in seq))


def sort_element(seq, element_index):
    v = seq[element_index]
    i = element_index - 1
    while seq[i] > v and i >= 0:
        seq[i + 1] = seq[i]
        i -= 1
    seq[i + 1] = v


def insertion_sort(seq):
    if len(seq) == 1:
        print_seq(seq)
        return
    for index in range(1, len(seq)):
        sort_element(seq, index)
        print_seq(seq)

S = int(input())
ar = [int(x) for x in input().split()]

insertion_sort(ar)
