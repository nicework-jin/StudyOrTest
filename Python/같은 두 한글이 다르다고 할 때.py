# https://jonsyou.tistory.com/26 참고

"""
a와 b가 같아 보이지만 1번 테스트에서는 다르다고 나옴
"""
# (1) False
a1 = '가장 큰 수'
b1 = '가장 큰 수'
print(a1.encode('utf8') == b1.encode('utf-8'))

# (2) True
a2 = '가장 큰 수'
b2 = '가장 큰 수'
print(a1.encode('utf8') == b1.encode('utf-8'))

"""
a1과 b1의 첫 번째 문자를 비교하면 차이를 발견할 수 있음.
"""

# ㄱ 가
print(a1[0], b1[0])

"""
해결방법 >>  unicodedata 모듈을 이용한다.
"""

import unicodedata

print(a1[0])  # ㄱ
a1 = unicodedata.normalize('NFC', a1)
print(a1[0])  # 가
