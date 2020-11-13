while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 입력값이 얼마나 들어올 지 모르기 때문에 try로 입력값을 받아보고
# True 일 경우 print(a+b)
# 입력값이 더이상 없거나 틀릴 경우 break