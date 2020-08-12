'''
작은 따옴표 3개를 연속으로 입력하면 Block comment라고 한다.
주석
'''

# random 모듈을 사용할 수 있도록 포함.
import random

# 함수 정의 시작
def lotto():
    # 1~45 정수중에서 6개를 무작위로 추출 / 리스트로 리턴
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    return lotto

print(lotto())

# 도큐멘트 스트링 사용방법
print(lotto.__doc__)
help(lotto)
