"""
Date: March 9, 2024
Name: Rajashree Dahal
Problem: You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor_list=[]
        count=1
        while len(factor_list)<=k and count<=n:
            if n % count==0:
                factor_list.append(count)
                count=count+1
            else:
                count=count+1
        if len(factor_list)<k:
            return -1
        return factor_list[k-1]