import sys
file = open('in.txt')
sys.stdin = file

T = int(input())

for _ in range(T):
    N, K = [int(x) for x in input().split()]
    on_time = 0
    for x in input().split():
        x = int(x)
        if x > 0:
            continue
        on_time += 1
    if K > on_time:
        print("YES")
    else:
        print("NO")
