import sys
from math import gcd

a, b = map(int, sys.stdin.readline().split())


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(a, b))
print(lcm(a, b))
