import sys

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = sys.stdin.readline().split()

b = int(b)
ans = 0

for idx, value in enumerate(n[::-1]):
    print(idx, value, b)
    ans += num_list.index(value) * (b ** idx)

print(ans)
