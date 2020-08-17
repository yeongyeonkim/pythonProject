# python 3의 변경.
print(1/2)
# 0.5
print(type(2**100))
# long -> int로 통일하였다.

###########

print("하나", "둘", "셋", 1, 2, 3, sep='-')

print("다른 줄에 출력")
print("다른 줄에 출력")
print("같은 줄에 출력", end="--->")
print("같은 줄에 출력")
print(20 * '-')
print("나의 이름은 '김영연'입니다.")
print('나의 이름은 "김영연"입니다.')
print("나의 이름은 \"김영연\"입니다.")
print('나의 이름은 \'김영연\'입니다.')
print('-' * 20)
print('나이는 {1}세이고, 성별은 {2}입니다. 나의 이름은 "{0}"입니다. '.format('김영연', 28, '남자'))
print('나이는 {age}, 성별은 {gender}, 이름은 {name}'.format(gender='남성',name='김영연',age=28))
print('-' * 20)
print('{:<15}'.format('왼쪽정렬'))
print('{:>15}'.format('오른쪽정렬'))
print('{:^15}'.format('가운데정렬'))
