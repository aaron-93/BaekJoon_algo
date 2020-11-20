# 문제
# 45656이란 수를 보자. 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.


# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[0][i] = 1

# 0번은 1자리수 (초기값) 이기 때문에 제외
for a in range(2, n + 1):
    for b in range(10):
        if b == 0:
            dp[a][b] = dp[a - 1][1]
        elif b == 9:
            dp[a][b] = dp[a - 1][9]
        else:
            dp[a][b] = dp[a - 1][b - 1] + dp[a - 1][b + 1]


# dp[n]은 10^n번째 자리, 즉 n=1 이면 10^1 = 두자리 수. 따라서 n-1 해줘야 원하는 자릿수가 나옴
print(sum(dp[n]) % 1000000000)

# 근데 틀림 ^~^


n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)

# 수정된 코드

# 풀이방법
# 리스트 초기화 = [0,0,0,0,0,0,0,0,0,0]
# N = 1일 때 = [1,1,1,1,1,1,1,1,1,1] (1의 자리에 0~9까지 1개씩 삽입가능, 0은 점화식을 위해 1)
# N = 2일 때, 첫 숫자가 1이라면 뒤에 0 과 2가 올 수 있음 0과 2가 오는 방법은 N=1 리스트에서 idx[1][0] 과 idx[1][2]
# 그러므로 [1,2,2,2,2,2,2,2,2,1] (10의자리에 9가 오면 1의자리는 무조건 8밖에 올 수 없음)
# N = 3 일때, 100의 자리에 1이 왔을 때 뒤에 올 수 있는 숫자 조합은 01,21,23 3가지,
# 위 3가지 숫자는 각 N=2 리스트에서 idx[2][0]과 idx[2][2]의 값
# 따라서 점화식은 dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# 하지만 0과 9는 각각 0으로 시작할 수 없고 1차이 나는 숫자는 오직 1, 9와 1차이 나는 수는 오직 8밖에 없으므로 점화식이 다름
# 0 점화식 = dp[i][j] = dp[i - 1][1] / 9 점화식 = dp[i][j] = dp[i - 1][8]