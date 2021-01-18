import sys
from decimal import Decimal, getcontext

a, b = map(str, sys.stdin.readline().split())
getcontext().prec = 1104

print("{0:f}".format(Decimal(a) ** int(b)))