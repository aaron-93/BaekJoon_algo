n = int(input())
dic = {}

for i in range(n):
    cur_card = int(input())
    if cur_card in dic:
        dic[cur_card] += 1
    else:
        dic[cur_card] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(dic[0][0])
