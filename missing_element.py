"Solution-1"
def missing_element(arr:list) -> int:
    for num in range(1,(len(arr)+1)):
        if num not in arr:
            return print(num)
missing_element([1,3,4])

"Solution-2"
def missing_element(arr:list) -> int:
    cur_sum = 0
    for i in arr:
        cur_sum += i 
    req_sum = 0
    for i in range(1,(len(arr)+1):
        req_sum += i
    return print(req_sum - cur_sum)
missing_element([1,3,4])
