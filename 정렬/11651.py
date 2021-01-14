n = int(input())
l = []


for i in range(n):
    a, b = list(map(int, input().split()))
    l.append([b, a])

sorted_l = sorted(l)

for i in sorted_l:
    print(i[1], i[0])
