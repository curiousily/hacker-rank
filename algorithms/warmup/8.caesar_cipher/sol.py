import sys
file = open('in.txt')
sys.stdin = file

import string
input()
cipher = input()
k = int(input())

text = ""

lower = string.ascii_lowercase
upper = string.ascii_uppercase

for ch in cipher:
    lst = [ch]
    if ch in lower:
        lst = lower
    elif ch in upper:
        lst = upper
    text += lst[(lst.index(ch) + k) % len(lst)]

print(text)
