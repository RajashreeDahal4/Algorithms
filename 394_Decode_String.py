"""
Date: February 5, 2024
Name: Rajashree Dahal
Problem: Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""
import re
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cur_str=""
        cur_num=0
        for c in s:
            if c.isdigit():
                cur_num=cur_num*10+int(c)
            elif c=="[":
                stack.append(cur_num)
                stack.append(cur_str)
                cur_num=0
                cur_str=""
            elif c=="]":
                prev_str=stack.pop()
                prev_num=stack.pop()
                cur_str=prev_str+cur_str*prev_num
            else:
                cur_str=cur_str+c
        return cur_str
            
