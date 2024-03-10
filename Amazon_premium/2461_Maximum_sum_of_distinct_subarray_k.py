"""
Date: March 10, 2024
Name: Rajashree Dahal
Problem:
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.
"""
class Solution:    
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        mp = defaultdict(int)
        currentSum = 0
        maxSum = 0
        n = len(arr)
        left = 0
        i = 0
    
        # Iterating for length k
        while i < k and i < n:
            currentSum += arr[i]
            mp[arr[i]] += 1
    
            i += 1
    
        # If distinct elements present in map
        # equal to k
        if len(mp) == k:
            maxSum = currentSum
        # Iterating over the left array
        for i in range(k, n):
            mp[arr[i]] += 1
            mp[arr[left]] -= 1
            if mp[arr[left]] == 0:
                del mp[arr[left]]
            currentSum += arr[i]
            currentSum -= arr[left]
            if len(mp) == k:
                maxSum = max(maxSum, currentSum)
            left += 1
    
        # Returning the maximum sum
        return maxSum