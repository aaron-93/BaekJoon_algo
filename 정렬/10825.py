n = int(input())
table = []

for i in range(n):
    table.append(list(input().split()))


table.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), (x[0])))

for i in range(len(table)):
    print(table[i][0])