import sys
file = open('in.txt')
sys.stdin = file

input()
inputs = input().split()
nums = [int(i) for i in inputs]
print(sum(nums))
