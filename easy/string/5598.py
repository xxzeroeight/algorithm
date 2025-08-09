"""
카이사르 암호 형식(3칸 건너뛴)으로 변환된 문자열을 원래 단어로 고친다.

예제 1:
입력: MRL
출력: JOI

예제 2:
입력: FURDWLD
출력: CROATIA

제약 조건:
단어는 최대 1000자 이하이다.
"""
import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
res = ""
for w in s:
    s = (ord(w) - 68) % 26

    res += chr(s+65)

# [결과 출력]
print(res)
