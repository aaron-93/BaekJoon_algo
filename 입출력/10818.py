# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.


a = int(input())
b = input().split()
list = []

for i in range(0, a):
    list.append(int(b[i]))

print(min(list), max(list))


# b는 공백으로 구분된 N개의 정수, input().split()으로 정수별 구분
# b는 N개의 문자열! 로 만들어진 리스트
# for 문을 이용, int로 리스트 b의 값을 list에 저장 후
# 최소값, 최대값 도출


# 맞춘 사람 중 짧은 코드

import sys

n, *m = map(int, sys.stdin.read().split())
print(min(m), max(m))

# sys 모듈 : 파이썬 인터프리터를 제어할 수 있는 방법을 제공 (https://wikidocs.net/78)
# sys.stin.readline() : 입력한 한 라인을 literable 한 컨테이너에 저장 (https://bnzn2426.tistory.com/105)
# 변수 : 프로그램 실행 중 상황에 따라 다른 값들을 표현할 수 있는 값
# 상수 : 프로그램 실행 중 항상 같은 값을 표현
# literal : 변수 및 상수에 저장되는 "값 자체"
# *m 이 의미하는 것 = 1개 이상의 인자