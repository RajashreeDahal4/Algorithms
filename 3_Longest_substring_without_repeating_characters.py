"""
Date: January 28, 2024
Name: Rajashree Dahal
Problem: Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self,string):
        substring_start=len_substring=0
        track={}
        for enum,each_string in enumerate(string):
            if track.get(each_string,-1)>=substring_start:
                substring_start=track[each_string]+1
            len_substring=max(len_substring,enum-substring_start+1)
            track[each_string]=enum
        return len_substring