"""
Date: February 10, 2024
Name: Rajashree Dahal
Problem:

Code
Testcase
Testcase
Test Result
14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return strs[0]
        end=min(len(strs[0]),len(strs[len(strs)-1]))
        i=0
        while (i<end and strs[0][i]==strs[len(strs)-1][i]):
            i=i+1
        pre=strs[0][0:i]
        return pre

