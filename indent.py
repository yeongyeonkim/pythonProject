"""
코딩의 가독성을 위해 들여쓰기를 한다.
다른 프로그램 언어에서는 {}를 사용하여 영역을 지정한다.
하지만 파이썬은 들여쓰기를 사용하여 영역을 지정한다.
"""

def line():
    print("-" * 30)
    
def show(char="★", count=5):
    """
    show 함수 : 지정문자를 지정한 갯수만큼 출력.
    show(char, count)
    첫번째 인수 : 출력할 문자(기본 값 : ★)
    두번째 인수 : 출력한 개수(기본 값 : 5)
    """
    print(char * count)
    line()
    
show()
show("◆")
# 인수에 기본 값을 정해 주었을 경우 뒤에서 부터 생략 가능
show(30)
show("o", 10)

# 1 1 2 3 5 8

def factorial(x):
    if x == 1 or x == 2:
        return 1
    else:
        return factorial(x - 1) + factorial(x - 2)

print(factorial(6), '팩토리얼 출력')