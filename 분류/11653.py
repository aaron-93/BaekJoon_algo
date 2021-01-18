import sys

n = int(sys.stdin.readline())

while n >= 2:
    answer = []
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            break
    n = n // i
