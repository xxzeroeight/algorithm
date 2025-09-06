"""
문자열이 주어지면, 이 중 그룹 단어를 센다.

예제 1:
입력:
3
happy
new
year
출력:
3

예제 2:
입력:
4
aba
abab
abcabc
a
출력:
1

예제 3:
입력:
5
ab
aa
aca
ba
bb
출력:
4

예제 4:
입력:
2
yzyzy
zyzyz
출력:
0

예제 5:
입력:
1
z
출력:
1

예제 6:
입력:
9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz
출력:
2

제약 조건:
N은 100보다 작거나 같은 자연수이다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

풀이:
1. 연속하다는 것은 중복하다는 것과 같다.
2. 스택을 이용하여 스택의 마지막 단어와 다음에 올 단어가 다른 경우에만 넣는다.
3. set()으로 중복을 제거한 단어와 스택의 단어가 일치하면 그 문자열은 그룹 단어이다. (정렬)
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

# [핵심 로직]
cnt = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()

    stack = []
    for w in s:
        if not stack:
            stack.append(w)

        if stack[-1] != w:
            stack.append(w)

    if sorted(list(set(s))) == sorted(stack):
        cnt += 1

# [결과 출력]
print(cnt)
