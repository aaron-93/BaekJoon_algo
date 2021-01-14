# 나의 풀이 - 오답
n = int(input())
l = []


for i in range(n):
    arr = list(map(int, input().split()))
    l.append(arr)

l = sorted(l)

for i in range(l):
    print(l)

# 2차 풀이

n = int(input())
l = []


for i in range(n):
    arr = list(map(int, input().split()))
    l.append(arr)

sorted_l = sorted(l)

for i in sorted_l:
    print(i[0], i[1])
