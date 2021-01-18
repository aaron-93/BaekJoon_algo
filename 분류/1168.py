import sys

n, k = map(int, sys.stdin.readline().split())

list = [i for i in range(1, n + 1)]
array = []
idx = 0

for i in range(n):
    idx += k - 1
    if idx >= len(list):
        idx = idx % len(list)
    array.append(str(list.pop(idx)))
print("<", ", ".join(array)[:], ">", sep="")
