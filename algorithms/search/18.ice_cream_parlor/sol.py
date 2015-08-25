import sys
file = open('in.txt')
sys.stdin = file

from collections import defaultdict


def print_seq(seq):
    print(' '.join('{}'.format(v) for v in seq))

T = int(input())

for _ in range(T):

    M = int(input())
    _ = input()
    prices = [int(x) for x in input().split()]

    if M % 2 == 0:
        indices = []
        for i, c in enumerate(prices):
            if c == M / 2:
                indices.append(i + 1)
        if len(indices) == 2:
            print_seq(sorted(indices))
            continue

    prices = defaultdict(int, {int(v): k + 1 for k, v in enumerate(prices)})

    for k in sorted(prices.keys()):
        n = M - k
        if prices[n] > 0 and n != k:
            indices = [prices[k], prices[n]]
            print_seq(sorted(indices))
            break
