import sys
sys.setrecursionlimit(3000)
input_file = open('input.txt', 'r')
input_arr=[]
for n in input_file:
    input_arr.append(int(n.strip()))


def getIncreasing(arr, n=0):
    if len(arr) == 1:
        return n
    else:
        if arr.pop(0) > arr[0]:
            return getIncreasing(arr, n)
        else:
            return getIncreasing(arr,n+1)
print(getIncreasing(input_arr))
