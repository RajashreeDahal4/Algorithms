"""
Date: January 26, 2024
Name: Rajashree Dahal
Problem: Given an integer array nums, return an array answer such that answer[i] is equal to the product of
 all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in 
a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1 for i in nums]
        prefix=1
        track_postfix=[1 for i in nums]
        for enum,i in enumerate(nums):
            result[enum]=prefix
            prefix=prefix*nums[enum]
        postfix=1
        post_result=[1 for i in nums]
        for i in range(len(nums)-1,-1,-1):
            post_result[i]=nums[i]*postfix
            postfix=post_result[i]
        final_result=[i if (enum+1)>(len(nums)-1) else i*post_result[enum+1] for enum,i in enumerate(result)]
        return final_result