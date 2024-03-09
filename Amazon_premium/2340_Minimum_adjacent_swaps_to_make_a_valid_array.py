"""
Date: March 9, 2024
Name: Rajashree Dahal
Problem: You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.
"""
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        # Find the index of the smallest and largest elements
        min_value = min(nums)
        min_index=[enum for enum,i in enumerate(nums) if i==min_value]
        min_index=min(min_index)
        max_value=max(nums)
        max_index=[enum for enum,i in enumerate(nums) if i==max_value]
        max_index=max(max_index)
        # Calculate the number of swaps to move the smallest element to the leftmost position
        left_swaps = min(min_index, n-1 - max_index)
        # Calculate the number of swaps to move the largest element to the rightmost position
        right_swaps = max(min_index, n - 1 - max_index) - (1 if min_index > max_index else 0)
        # return max(left_swaps, right_swaps)
        return left_swaps+right_swaps