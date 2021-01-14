import sys
from collections import deque


def push(value):
    queue.append(value)


def pop():
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()


def size():
    return len(queue)


def empty():
    if size() == 0:
        return 1
    else:
        return 0


def front():
    if len(queue) == 0:
        return -1
    else:
        return queue[0]


def back():
    if len(queue) == 0:
        return -1
    else:
        return queue[-1]


n = int(sys.stdin.readline())
queue = deque()


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
    elif operation == "front":
        print(front())
    elif operation == "back":
        print(back())
