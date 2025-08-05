"""
어떤 단어가 주어졌을 때, "CAMBRIDGE"에 포함된 알파벳을 삭제한다.

예제 1:
입력: LOVA
출력: LOV

예제 2:
입력: KARIJERA
출력: KJ

제약 조건:
알파벳 대문자로 이루어진 단어가 주어진다.
이 단어는 적어도 3글자이며, 많아야 100글자이다.
"""
import sys

# [입력 처리]
word = sys.stdin.readline().rstrip()

# [핵심 로직]
res = ""
for w in word:
    if w not in "CAMBRIDGE":
        res += w

# [결과 출력]
print(res)
