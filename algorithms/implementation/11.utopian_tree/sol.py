import sys
file = open('in.txt')
sys.stdin = file


def calculate_height(n):
    if n % 2 == 0:
        return pow(2, n / 2 + 1) - 1
    else:
        return pow(2, (1+(n+1)/2))-2

T = int(input())

for _ in range(T):
    cycles = int(input())
    print(int(calculate_height(cycles)))
