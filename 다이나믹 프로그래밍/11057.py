n = int(input())

# 리스트 초기화, n자리까지 만들어야 해서 n+1까지
dp = [[0 for i in range(10)] for j in range(n + 1)]

# N=1 일떄의 만들 수 있는 수의 갯수
for a in range(10):
    dp[0][a] = 1
# N>=2 일때 만들 수 있는 경우의 수
for b in range(0, n + 1):
    for v in range(10):
        # 0으로 시작 할 때
        if v == 0:
            dp[b][0] = sum(dp[b - 1])
        # 9로 시작 할 때
        elif v == 9:
            dp[b][9] = 1
        # 그 외의 수
        else:
            dp[b][v] = dp[b][v - 1] - dp[b - 1][v - 1]

print(sum(dp[n]) % 10007)
