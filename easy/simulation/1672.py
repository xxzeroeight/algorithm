"""
염기서열이 주어지면, 제일 끝에 있는 두 개의 염기를 새로운 염기로 바꾼다.

예제 1:
입력:
6
AAGTCG
출력:
A

제약 조건:
1 ≤ N ≤ 1,000,000
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())

di = {"AA": "A", "AG": "C", "AC": "A", "AT": "G",
      "GA": "C", "GG": "G", "GC": "T", "GT": "A",
      "CA": "A", "CG": "T", "CC": "C", "CT": "G",
      "TA": "G", "TG": "A", "TC": "G", "TT": "T"}

# [핵심 로직]
for _ in range(n-1):
    old = s[-1] + s[-2]
    new = di[old]
    s.pop()
    s.pop()
    s.append(new)

# [결과 출력]
print(*s)
