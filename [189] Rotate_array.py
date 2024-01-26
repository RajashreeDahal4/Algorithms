"""
Date: January 26, 2024
Name: Rajashree Dahal
Problem: Given an integer array nums, 
rotate the array to the right by k steps, 
where k is non-negative.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)==0:
            return []
        if k==0:
            return nums
        if nums is not None:
            if len(nums)<k:
                nums=Solution.rotate(self,nums,len(nums))
                nums=Solution.rotate(self,nums,k-len(nums))
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        return nums
