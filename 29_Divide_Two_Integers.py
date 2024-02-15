"""
Date: February 15, 2024
Name: Rajashree Dahal
Problem: Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""
import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0) else 1
        dividend=abs(dividend)
        divisor=abs(divisor)
        result=len(range(0,dividend-divisor+1,divisor))
        if sign==-1:
            result=-result
        if result<-2**31:
            return -2**31
        elif result>2**31-1:
            return 2**31-1
        return result
        