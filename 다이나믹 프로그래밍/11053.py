# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은
# A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 다른 사람 풀이
n = int(input())
dp = [0] * (n + 1)
arr = list(map(int, input().split()))

for i in arr:
    dp[i] = max(dp[:i]) + 1


print(max(dp))

# 나의 풀이

n = int(input())
dp = [0] * n
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
