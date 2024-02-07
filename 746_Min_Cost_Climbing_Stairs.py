"""
Date: February 6, 2024
Name: Rajashree Dahal
Problem: You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length=len(cost)
        dp=[0]*length
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,length):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[length-1],dp[length-2])
