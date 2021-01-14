n, k = map(int, input().split())
max_number = 1000000000
table = [1]
table += [0] * n

for _ in range(1, k + 1):
    for idx in range(1, n + 1):
        table[idx] = (table[idx] + table[idx - 1]) % max_number

print(str(table[n]))