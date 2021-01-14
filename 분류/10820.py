while True:
    try:
        n = input()
        upper = 0
        lower = 0
        num = 0
        space = 0
        for i in range(len(n)):
            if ord(n[i]) == 32:
                space += 1
            elif 65 <= ord(n[i]) <= 90:
                upper += 1
            elif 97 <= ord(n[i]) <= 122:
                lower += 1
            else:
                num += 1
        print(lower, upper, num, space)
        upper = 0
        lower = 0
        num = 0
        space = 0
    except EOFError:
        break