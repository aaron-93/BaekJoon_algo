while True:
    try:
        a = input()
        print(a)
    except a != type(int) or type(str):
        break

# 입력 받은 대로 출력하는 프로그램을 작성하시오.
# 입력값 = 최대 100줄 / 알파벳 소문자, 대문자, 공백, 숫자로만 / 100글자 이하 / 빈줄 X
# (이어서) 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

# 위 풀이의 문제점 : 숫자엔 정수,소수,실수 등 다양한 값이 존재하지만 type(int)는 정수만 처리, 따라서 틀릴 가능성 있음

while True:
    try:
        print(input())
    except EOFError:
        break

# 입력받은 값을 그대로 print 함
# EOFError 가 발생하면 종료
# EOFError = End Of File error
#   input() 함수가 데이터를 읽지 못한 상태에서 EOF (end-of-file) 조건을 만날 때 발생합니다.
#   (주의하세요: io.IOBase.read() 와 io.IOBase.readline() 메서드는 EOF를 만날 때 빈 문자열을 돌려줍니다.)
#  - 파이썬 공식문서 (https://docs.python.org/ko/3/library/exceptions.html)