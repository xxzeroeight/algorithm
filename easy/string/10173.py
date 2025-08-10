"""
문자열에서 니모(대소문자 상관없음)를 찾는다.

예제 1:
입력:
Marlin names this last egg Nemo, a name that Coral liked.
While attempting to save nemo, Marlin meets Dory,
a good-hearted and optimistic regal blue tang with short-term memory loss.
Upon leaving the East Australian Current,(888*%$^&%0928375)Marlin and Dory
NEMO leaves for school and Marlin watches NeMo swim away.
EOI
출력:
Found
Found
Missing
Missing
Found
"""

import sys

# [입력 처리]
while 1:
    sentense = sys.stdin.readline().rstrip()

# [핵심 로직]
    if sentense == "EOI":
        break

# [결과 출력]
    print("Found" if "nemo" in sentense.lower() else "Missing")
