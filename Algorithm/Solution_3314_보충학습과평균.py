"""
<input>
1
10 65 100 30 95
<output>
#1 68
"""
T = int(input())

for t in range(1, T+1):
    avg = 0
    arr = list(map(int, input().split()))
    for idx in arr:
        avg += idx if idx >= 40 else 40
    print("#{0} {1}".format(t, avg//5))
"""
<short coding>
for t in range(1, int(input()) + 1):
    print(f'#{t} {sum([i if i >= 40 else 40 for i in map(int, input().spilt())])//5')
"""