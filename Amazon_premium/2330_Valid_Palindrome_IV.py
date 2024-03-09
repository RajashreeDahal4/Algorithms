"""
Date: March 9, 2024
Name: Rajashree Dahal
Problem: You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.
Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.
"""
import math
from collections import Counter
class Solution:
    def makePalindrome(self, s: str) -> bool:
        if len(s)<=3:
            return True
        else:
            left=0
            right=len(s)-1
            tracker=[]
            while left<right:
                if s[left]!=s[right]:
                    tracker.append(left)
                left=left+1
                right=right-1
            if len(tracker)==0 or len(tracker)<=2:
                return True
            return False

