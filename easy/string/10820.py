"""
문자열이 주어지면, 소문자, 대문자, 숫자, 공백을 센다.

예제 1:
입력:
This is String
SPACE    1    SPACE
 S a M p L e I n P u T
0L1A2S3T4L5I6N7E8
출력:
10 2 0 2
0 10 1 8
5 6 0 16
0 8 9 0

제약 조건:
1 ≤ N ≤ 100
"""

# [입력 처리]
while 1:
    try:
        s = input()

        l, u, n, p = 0, 0, 0, 0
        for w in s:
            if w.islower():
                l += 1
            elif w.isupper():
                u += 1
            elif w.isnumeric():
                n += 1
            else:
                p += 1

        print(l, u, n, p)

# [핵심 로직]


# [결과 출력]
    except:
        break
