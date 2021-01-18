import sys
from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


n = int(input())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    print(lcm(x, y))
