import sys
from collections import deque


def push_front(value):
    queue.appendleft(value)


def push_back(value):
    queue.append(value)


def pop_front():
    if len(queue) == 0:
        return -1
    else:
        return queue.popleft()


def pop_back():
    if len(queue) == 0:
        return -1
    else:
        return queue.pop()


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

    if operation == "push_front":
        push_front(order[1])
    elif operation == "push_back":
        push_back(order[1])
    elif operation == "pop_front":
        print(pop_front())
    elif operation == "pop_back":
        print(pop_back())
    elif operation == "size":
        print(size())
    elif operation == "empty":
        print(empty())
    elif operation == "front":
        print(front())
    elif operation == "back":
        print(back())
