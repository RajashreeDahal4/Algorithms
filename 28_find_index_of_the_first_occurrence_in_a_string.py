"""
Date: February 15, 2024
Name: Rajashree Dahal
Problem: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            index=re.finditer(needle,haystack)
            positions = [match.start() for match in index]
            first_position=positions[0]
        return first_position