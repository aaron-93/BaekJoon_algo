r = int(input())
for idx in range(r):
    a, b = map(int, input().split())
    print(f"Case #{idx+1}: {a+b}")

# 가장 처음 값은 입력받을 입력값의 갯수
# 출력형식이 Case #n: value 형식이기 때문에 print(f"Case #{idx+1}: {a+b}")
# 인덱스의 첫번째는 0으로 시작하기 때문에 idx+1 으로 출력