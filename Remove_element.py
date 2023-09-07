"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
#Solution-1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums=[]
        for i in nums:
            if i!=val:
                new_nums.append(i)
        nums[:]=new_nums
        return len(nums)
#Solution-2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:]=[i for i in nums if i!=val]
        return(len(nums))

  
