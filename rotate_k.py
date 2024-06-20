""" Program to rotate and reverse the array using a k-value
 Input = [1,2,3,4,5,6,7,8,9] , k = 2
 Output = [9, 8, 1, 2, 3, 4, 5, 6, 7] """

def rotate(arr:list,k:int) -> list:
    rotated_list = arr[len(arr)-k:len(arr):][::-1]+arr[0:len(arr)-k:]
    return rotated_list
rotate([1,2,3,4,5,6,7,8,9],2)

"""The time complexity of the solution is O(n)"""
