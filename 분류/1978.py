import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if arr[i] == 1:
        n -= 1
    else:
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                n -= 1
                break

print(n)