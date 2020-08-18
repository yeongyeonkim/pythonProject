"""
<input>
4
3 5
1 0 0 1 0
1 1 1 0 0
0 0 0 1 0
4 4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
4 4
0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0
1 1
0
<output>
#1 1 3
#2 4 4
#3 4 3
#4 1 0
"""
T = int(input())

for t in range(1, T+1):
    cnt = 0
    top = 0
    nm = list(map(int, input().split()))
    for i in range(0, nm[0]):
        tmp = 0
        arr = list(map(int, input().split()))
        for num in arr:
            if num == 1:
                tmp = tmp + 1
        if tmp == top:
            cnt = cnt + 1
        if tmp > top:
            top = tmp
            cnt = 1
    print("#{0} {1} {2}".format(t,cnt,top))