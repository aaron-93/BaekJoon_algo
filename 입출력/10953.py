r = int(input())
for idx in range(r):
    a, b = map(int, input().split(","))
    print(a + b)


# 가장 처음 입력값은 총 입력될 입력값의 갯수
# 모든 입력값은 ,로 구분되어 있기 때문에 split(",")
