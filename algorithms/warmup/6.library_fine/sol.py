import sys
file = open('in.txt')
sys.stdin = file

D, M, Y = input().split()
D, M, Y = int(D), int(M), int(Y)
d, m, y = input().split()
d, m, y = int(d), int(m), int(y)


def calc_hackos():
    if y > Y:
        return 0
    if y == Y and m > M:
        return 0
    if y == Y and m == M and d >= D:
        return 0

    if Y > y:
        return 10000
    if M > m:
        return 500 * (M - m)
    if D > d:
        return 15 * (D - d)

print(calc_hackos())
