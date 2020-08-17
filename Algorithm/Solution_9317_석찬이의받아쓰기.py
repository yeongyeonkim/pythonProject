"""
<input>
2
16
MyNameIsSeokChan
mynameisseokchan
15
SamsungSoftware
MembershipZzang
<output>
#1 11
#2 2
"""
T = int(input())

for t in range(1, T+1):
    cnt = 0
    n = int(input())
    str1 = input()
    str2 = input()
    for idx in range(0, n):
        if(str1[idx].__eq__(str2[idx])):
            cnt = cnt + 1
    print("#{0} {1}".format(t, cnt))