"""
단어가 주어지면, 주어진 조건에 맞는 단어를 출력한다.

예제 1:
입력:
mobitel
출력:
bometil

제약 조건:
길이는 3 이상 50 이하이다.

풀이:
1. 단어를 세 부분으로 나누고, 각 부분을 뒤집는다.
2. 1에서 구한 모든 단어 중 사전순으로 가장 앞서는 것을 출력한다.
"""

import sys

# [입력 처리]
words = sys.stdin.readline().rstrip()

# [핵심 로직]
ans = []
for i in range(len(words)-2):
    for j in range(i+1, len(words)-1):
            ans.append(words[:i+1][::-1] + words[i+1:j+1][::-1] + words[j+1:][::-1])

ans.sort()

# [결과 출력]
print(ans[0])
