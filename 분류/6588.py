import sys

r = 1000000


def get_prime_list(r):
    sieve = [True] * r
    m = int(r ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, r, i):
                sieve[j] = False
    return [[i for i in range(2, r) if sieve[i] == True], sieve]


p_number = get_prime_list(r)[0]
p_checker = get_prime_list(r)[1]

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(n // 2):
        if p_checker[n - p_number[i]] == True:
            print(f"{n} = {p_number[i]} + {n-p_number[i]}")
            break