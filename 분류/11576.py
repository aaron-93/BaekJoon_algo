import sys

a, b = map(int, sys.stdin.readline().split())
n = int(input())

a_digit = list(map(int, sys.stdin.readline().split()))
ten_digit = 0
ans = []

for i in range(n):
    ten_digit += a_digit[-1] * (a ** i)
    a_digit.pop(-1)
while ten_digit != 0:
    ans.append(str(ten_digit % b))
    ten_digit = ten_digit // b

print(" ".join(ans[::-1]))
