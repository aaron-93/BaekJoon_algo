# 문제

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#   1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
#   2. X가 2로 나누어 떨어지면, 2로 나눈다.
#   3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
#  #첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 입력받을 값 = x
x = int(input())

# x+1 길이의 리스트, 인덱스는 n번째 수, 인덱스 값은 연산 최소값
result = [0 for _ in range(x + 1)]

# 0 과 1은 의미가 없기 때문에 2번부터 생각한다
for i in range(2, x + 1):
    # i가 될 수 있는 확실한 방법 = i-1 에서 1을 더하는 것
    result[i] = result[i - 1] + 1
    # 만약 i가 2의 배수라면 i 이전의 가장 큰 2의 배수에서 2를 곱하는게 연산을 최소화 할 수 있음
    # 현재 for문에서 가장 기본적인 연산은 무조건 앞의 수에서 1을 더해주는 것
    # 1부터 i까지 계속 1씩 더하는 방법은 비효율
    # 그렇기 때문에 result[i] > result[i // 2] + 1 를 검사해봐서  i-1에서 1을 더하는 것 보다
    # i 이전의 가장 큰 2의배수에서 2를 곱하는것이 더 효율적일 때 i//2를 만드는 방법 수에 +1을 더해줌

    # eg) 4를 만들기 위해선 1에서부터 1을 세번 더하는 방법 (연산 3회), 2를 만든 후 *2 하는 방법(연산 2회),
    # 3을 만든 후 1을 더하는 방법 (3을 만드는 연산 +1회)이 있는데
    # 만약 3까지 도달 후 4가 되는 과정이 2에 도달 후 *2 연산을 하는 과정보다 길 경우 (result[4]값이 result[2] +1보다 클 경우)
    # 더 작은 방법을 선택 (result[4] = result[2]+1)

    if i % 2 == 0 and result[i] > result[i // 2] + 1:
        result[i] = result[i // 2] + 1
    # 만약 i가 3의 배수라면 i 이전의 가장 큰 3의 배수에서 3을 곱하는게 연산을 최소화 할 수 있음
    if i % 3 == 0 and result[i] > result[i // 3] + 1:
        result[i] = result[i // 3] + 1

print(result[x])