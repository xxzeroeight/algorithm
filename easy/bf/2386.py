"""
알파벳 단어와 문장이 주어지면, 문장에서 단어가 몇 번 나타나는지 센다.

예제 1:
입력:
g Programming Contest
n New Zealand
x This is quite a simple problem.
#
출력:
g 2
n 2
x 0

제약 조건:
각 문장은 길이가 1에서 250이다.
"""
import sys

# [입력 처리]
while 1:
    sentense = list(sys.stdin.readline().split())

# [핵심 로직]
    a = sentense[0]
    s = sentense[1:]

    if a == "#":
        break

    cnt = 0
    for w in s:
        cnt += w.lower().count(a)

# [결과 출력]
    print(a, cnt)
