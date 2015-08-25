import sys
file = open('in.txt')
sys.stdin = file

T = int(input())

for _ in range(T):
    string = input()
    prev_char = 'B' if string[0] == 'A' else 'A'
    deletions = 0
    for ch in string:
        if ch == prev_char:
            deletions += 1
        else:
            prev_char = ch
    print(deletions)
