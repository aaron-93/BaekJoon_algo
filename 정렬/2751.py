import sys

n = int(input())
list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))

for i in sorted(list):
    sys.stdout.write(str(i) + "\n")
