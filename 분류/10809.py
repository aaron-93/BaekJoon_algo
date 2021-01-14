n = input()
count = [-1 for i in range(26)]


for i in range(len(n)):
    idx = ord(n[i])
    if count[idx - 97] == -1:
        count[idx - 97] = i


for i in count:
    print(i, end=" ")