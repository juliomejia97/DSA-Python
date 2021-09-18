import math


def max_sub_array_sum(arr):
    maxSum = -math.inf
    maxHere = 0
    for i in range(len(arr)):
        maxHere += arr[i]
        if maxHere > maxSum:
            maxSum = maxHere
        if maxHere < 0:
            maxHere = 0
    return maxSum


print(max_sub_array_sum([1, 2, 3, -2, 5]))
