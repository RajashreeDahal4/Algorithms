"""
Date: February 10, 2024
Name: Rajashree Dahal
Problem: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = 0
        negative = False  
        if x < 0:
            negative = True
            x = -x       
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > 7):
                return 0
            if (result < INT_MIN // 10) or (result == INT_MIN // 10 and digit < -8):
                return 0
            
            result = result * 10 + digit
        
        return -result if negative else result