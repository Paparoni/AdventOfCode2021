# For Part 2

import sys
sys.setrecursionlimit(3000)
# open our input file and put each line into an array
input_file = open('input.txt', 'r')
input_arr=[]
for n in input_file:
    input_arr.append(int(n.strip()))


def getIncreasing(arr, n=0):
    if len(arr) == 3:
        return n
    else:
        sum1 = arr.pop(0) + arr[0] + arr[1]
        sum2 = arr[0] + arr[1] + arr[2]
        if sum1 > sum2 or sum1 == sum2:
            return getIncreasing(arr, n)
        else:
            return getIncreasing(arr,n+1)

print(getIncreasing(input_arr))
