"""
사람의 성이 하이픈으로 구분된 문자열이 주어진다.
이 문자열을 짧은 형태(성의 첫 글자만 딴)로 출력한다.

예제 1:
입력: Knuth-Morris-Pratt
출력: KMP

예제 2:
입력: Mirko-Slavko
출력: MS

예제 3:
입력: Pasko-Patak
출력: PP

제약 조건:
입력은 한 줄로 이루어져 있고, 최대 100글자의 영어 알파벳 대문자, 소문자, 그리고 하이픈 ('-', 아스키코드 45)로만 이루어져 있다.
첫 번째 글자는 항상 대문자이다.
그리고, 하이픈 뒤에는 반드시 대문자이다.
그 외의 모든 문자는 모두 소문자이다.
"""

import sys

# [입력 처리]
sentence = sys.stdin.readline().rstrip().split("-")

# [핵심 로직]


# [결과 출력]
print("".join(word[0] for word in sentence))
