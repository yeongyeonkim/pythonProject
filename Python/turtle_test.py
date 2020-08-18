# turtle 사용
import turtle

# 일시정지
# turtle.done()

turtle.title('거북아 놀자!!') # 윈도우 제목
turtle.shape('turtle') #모양을 거북이로
turtle.color('black','red') # 색상변경
turtle.pu(); # 펜 들어
turtle.write("거북아 놀자!!") # 문자열 출력
turtle.fd(80) # 앞으로 80만큼 이동
turtle.pd(); # 펜 내려
turtle.bk(100) # 뒤로 100만큼 이동
turtle.left(90); turtle.fd(18); # 왼쪽으로 90도 회전 앞으로 18이동
turtle.color('black', 'red') # 거북이 색상 변경
turtle.stamp() # 도장 찍기
turtle.right(90); turtle.fd(110); # 오른쪽으로 90도 회전 앞으로 110이동
turtle.color('black', 'green') # 거북이 색상 변경
turtle.stamp() # 도장 찍기
turtle.right(90); turtle.fd(18); # 오른쪽으로 90도 회전 앞으로 18이동
turtle.color('black', 'yellow') # 거북이 색상 변경
turtle.stamp() # 도장 찍기
turtle.right(90); turtle.fd(110); # 오른쪽으로 90도 회전 앞으로 110이동
turtle.color('black', 'blue') # 거북이 색상 변경
turtle.stamp() # 도장 찍기
turtle.left(180); #  180도 회전
turtle.exitonclick() # 마우스로 클릭시 윈도우 종료

