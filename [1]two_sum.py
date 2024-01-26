"""
Date: Jan 25, 2024
Name: Rajashree Dahal
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target.You may assume that each input would have exactly 
one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        dict_rec={}
        for enum,i in enumerate(nums):
            if (target-i) in nums[enum+1:]:
                result.append(enum)
                result.append(nums[enum+1:].index(target-i)+enum+1)
                return result
            else:
                continue
        