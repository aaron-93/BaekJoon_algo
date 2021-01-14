import sys


def push(value):
    stack.append(value)


def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if size() == 0:
        return 1
    else:
        return 0


def top():
    if size() == 0:
        return -1
    else:
        return stack[-1]


n = int(sys.stdin.readline())
stack = []


for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    operation = order[0]

    if operation == "push":
        push(order[1])
    elif operation == "pop":
        print(pop())
    elif operation == "size":
        print(size())
    elif operation == "empty":
        print(empty())
    elif operation == "top":
        print(top())
