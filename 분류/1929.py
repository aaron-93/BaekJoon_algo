import sys


def isPrime(v):
    if v == 1:
        return False
    else:
        for i in range(2, int(v ** 0.5) + 1):
            if v % i == 0:
                return False
        return True


m, n = map(int, sys.stdin.readline().split())
for i in range(m, n + 1):

    if isPrime(i):
        print(i)
