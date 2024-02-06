"""
Date: February 6, 2024
Name: Rajashree Dahal
Problem: The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

"""
class Solution:
    def tribonacci(self, n: int,tracker=None) -> int:
        if n<0:
            return 0
        if tracker is None:
            tracker=[0]*(n+1)
            tracker[0]=0
            if n>=1:
                tracker[1]=1
            if n>=2:
                tracker[2]=1
        if n in [0,1,2]:
            return tracker[n]
        elif tracker[n]!=0:
            return tracker[n]
        else:
            tracker[n]=self.tribonacci(n-1,tracker)+self.tribonacci(n-2,tracker)+self.tribonacci(n-3,tracker)
            return tracker[n]
        