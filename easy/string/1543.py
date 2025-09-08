"""
각각 문자열로 이루어진 문서와 단어가 주어졌을 때, 문서에서 단어가 몇 번 등장하는지 센다.
단, 중복되면 안된다. (인덱스가 겹치면 안된다.)

예제 1:
입력:
ababababa
aba
출력:
2

예제 2:
입력:
a a a a a
a a
출력:
2

예제 3:
입력:
ababababa
ababa
출력:
1

예제 4:
입력:
aaaaaaa
aa
출력:
3

제약 조건:
문서의 길이는 최대 2500이다.
검색하고 싶은 단어의 길이는 최대 50이다.

풀이:
1. 검색 단어를 찾기 위해 인덱스를 하나씩 이동하면서 찾는다.
2. 검색 단어를 찾으면 검색 단어의 길이만큼 띄어서 다시 검색한다. (인덱스가 겹치면 안된다.)
"""

import sys

# [입력 처리]
text = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()

# [핵심 로직]
cnt, i = 0, 0
while 1:
    if i > (len(text) - len(find)):
        break

    if text[i:i+len(find)] == find:
        cnt += 1
        i += len(find)
    else:
        i += 1

# [결과 출력]
print(cnt)
