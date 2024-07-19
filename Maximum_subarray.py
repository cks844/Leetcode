""" Finding maximum sum of subarray using Kadane's algorithm"""

def max_subarray(arr:list) -> int :
    cur_sum = 0
    max_sum = float('-inf')
    for num in range(len(arr)):
        cur_sum += arr[num] 
        max_sum = max(max_sum,cur_sum)
        if cur_sum < 0:
            cur_sum = 0 
    return print(max_sum)
max_subarray([-2,7,-3,4])     