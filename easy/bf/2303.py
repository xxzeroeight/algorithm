"""
카드의 합의 일의 자리 수가 가장 큰 사람의 번호를 출력한다.

예제 1:
입력:
3
7 5 5 4 9
1 1 1 1 1
2 3 3 2 10
출력:
1

제약 조건:
N은 2이상 1,000이하이다.

풀이:
1. 각 사람의 카드의 합의 일의 자리 수를 리스트에 저장한다.
2. 가장 큰 수를 갖는 사람이 두 명 이상일 경우의 케이스를 위해 해당하는 사람을 다른 리스트에 담는다.
3. 점수가 가장 큰 사람의 번호를 출력한다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

# [핵심 로직]
li = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))

    mv = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                mv = max(mv, (nums[i]+nums[j]+nums[k])%10)

    li.append(mv)

# [결과 출력]
ans = [p for p in range(len(li)) if li[p] == max(li)]

if li.count(max(li)) >= 2:
    print(ans[-1]+1)
else:
    print(ans[0]+1)
