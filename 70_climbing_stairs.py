"""
Date: January 30, 2024
Name: Rajashree Dahal
Problem: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int,answer=None) -> int:
        if answer is None:
            answer={i:0 for i in range(1,n+1)}
            answer[1]=1
            if n>=2:
                answer[2]=2
        if answer[n]!=0:
            return answer[n]
        else:
            answer[n]= self.climbStairs(n-1,answer)+self.climbStairs(n-2,answer)
            return answer[n]
