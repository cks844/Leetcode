def sub_arr_sum(arr,k):
    sub_arr = []
    for i in range(len(arr)-k+1):
        window = arr[i:i+k]
        max_window = max(window)
        sub_arr.append(max_window)
    return print(sub_arr)


sub_arr_sum([1,3,-1,-3,5,3,6,7],3)


    

