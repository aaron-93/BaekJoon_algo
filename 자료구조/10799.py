array = list(input())
stack = []
chunk = 0

for i in range(len(array)):
    if array[i] == "(":
        stack.append("(")
    else:
        if array[i - 1] == "(":
            stack.pop()
            chunk += len(stack)
        else:
            stack.pop()
            chunk += 1

print(chunk)
