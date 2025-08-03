"""
# 문제 정보

문제: [2진수 8진수]
출처: [백준 1373]
난이도: [B1]
분류: [문자열]
"""

"""
# 메모

아이디어
 - 2진수 -> 10진수 -> 8진수
주의 사항
 - 8진수로 변환 후 접두어 제거
개선점
"""

import sys

# [입력 처리]
bi = sys.stdin.readline().rstrip()

# [핵심 로직]
de = int(bi, 2)
result = oct(de)

# [결과 출력]
print(result[2:])
