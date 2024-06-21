def selection_sort(arr:list)->list :
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return print(arr)
 
selection_sort([64,25,22,12,11])       