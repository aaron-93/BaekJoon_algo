import sys

n = int(sys.stdin.readline())


def neg_bin(t, d):
    if t == 0:
        return "0"
    else:
        if t % 2 == 0:
            return neg_bin(t // d, d) + "0"
        else:
            return neg_bin(t // d + 1, d) + "1"


ans = neg_bin(n, -2)

if ans == "0":
    print(ans)
else:
    print(ans[1:])