import sys

string = sys.stdin.readline().strip()
n = int(input())
q1 = list(s for s in string)
q2 = []


for i in range(n):
    cursor = len(q1)
    cmd = sys.stdin.readline().strip().split()
    op = cmd[0]
    if op == "L":
        if cursor > 0:
            q2.append(q1.pop())
    elif op == "D":
        if len(q2) > 0:
            q1.append(q2.pop())
    elif op == "B":
        if cursor > 0:
            q1.pop()
    elif op == "P":
        q1.append(cmd[1])

print("".join(q1 + list(reversed(q2))))
