"""
<Input>
2
182 371 29 49 28 21 928 11 5 1
13 400 3010 2011 1111 40 4 103 301 100111
<Output>
#1 19 1
#2 4 4
"""
import sys

T = int(input())

for t in range(1, T+1):
    max = -sys.maxsize
    min = sys.maxsize
    arr = list(input().split())
    for s in range(len(arr)):
        sum = 0
        for i in range(len(arr[s])):
            sum += int(arr[s][i])
        max = sum if sum > max else max
        min = sum if sum < min else min
    print("#{0} {1} {2}".format(t, max, min))