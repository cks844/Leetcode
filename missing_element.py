def missing_element(arr:list) -> int:
    cur_sum = 0
    for i in arr:
        cur_sum += i 
    req_sum = 0
    for i in range(arr[0],arr[len(arr)-1]+1):
        req_sum += i
    return print(req_sum - cur_sum)
missing_element([1,2,3,5])