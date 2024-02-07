"""
Date: February 6, 2024
Name: Rajashree Dahal
Problem: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*2 for i in range(n)]
        for i in range(0,n):
            dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1])
            dp[i][0] = dp[i-1][1]
        return dp[n-1][1]
            
