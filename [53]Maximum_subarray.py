"""
Date: January 24, 2024
Name: Rajashree Dahal
Problem: Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.


"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value,sum_val=nums[0],nums[0]
        for k,_ in enumerate(nums):
            if k==0:
                continue
            else:
                sum_val=max(nums[k],sum_val+nums[k])
                max_value=max(max_value,sum_val)
        return max_value