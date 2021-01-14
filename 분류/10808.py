n = input()
count = [0 for i in range(26)]


for i in range(len(n)):
    idx = ord(n[i])
    count[idx - 97] += 1

for i in count:
    print(i, end=" ")