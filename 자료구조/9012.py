# n = int(input())
# for _ in range(n):
#     stack = []
#     vps = input()
#     idx = 0
#     for s in vps:
#         if s == "(":
#             stack.append(s)
#         elif s == ")":
#             if len(stack) == 0:
#                 print("NO")
#                 idx = 1
#                 break
#             else:
#                 stack.pop()

#     if len(stack) != 0 and idx == 0:
#         print("NO")
#     elif len(stack) == 0 and idx == 0:
#         print("YES")


num = int(input())
for i in range(num):

    vps = list(input())
    while len(vps) != 0:
        if vps[0] == ")":
            print("NO")
            break
        else:
            if ")" in vps:
                vps.remove(")")
                vps.remove("(")
            else:
                print("NO")
                break
    if len(vps) == 0:
        print("YES")
