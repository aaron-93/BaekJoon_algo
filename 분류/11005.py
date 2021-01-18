import sys

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

n, b = map(int, sys.stdin.readline().split())

while n != 0:
    answer += str(num_list[n % b])
    n = n // b

print(answer[::-1])