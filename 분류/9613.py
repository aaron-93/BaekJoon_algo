import sys
from itertools import combinations
from math import gcd


n = int(sys.stdin.readline())


for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for combi in combinations(line[1:], 2):
        ans += gcd(combi[0], combi[1])
    print(ans)
