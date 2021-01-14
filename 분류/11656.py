n = input()
list = []
for i in range(len(n)):
    list.append(n[i:])

for i in sorted(list):
    print(i)