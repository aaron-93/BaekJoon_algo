while True:
    a, b = map(int, input().split())
    if a and b != 0:
        print(a + b)
    else:
        break

    # 가장 마지막 입력값은 입력값으로 0 0 을 갖기 때문에
    # if a,b == 0 이면 break로 종료