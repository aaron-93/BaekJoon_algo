# import sys

# l, k = map(int, sys.stdin.readline().split())

# list = list(map(int, sys.stdin.readline().split()))
# list = sorted(list)

# print(list[k - 1])


n, m = map(int, input().split())

list = list(map(int, input().split()))
print(sorted(list)[m - 1])
