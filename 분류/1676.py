import sys
import math

n = int(sys.stdin.readline())
factorial = str(math.factorial(n))

while True:
    count = 0
    for i in range(len(factorial) - 1, 1, -1):
        if factorial[i] == "0":
            count += 1
        else:
            break
    break


print(count)