"""
Date: March 9, 2024
Name: Rajashree Dahal
Problem: Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.
Note that each character should belong to exactly one substring in a partition.
"""
class Solution:
    def partitionString(self, s: str) -> int:
        substring_list=[]
        is_continuous=0
        for each_char in s:
            if not substring_list:
                substring_list.append(each_char)
                is_continuous=1
            else:
                if each_char in substring_list[-1]:
                    substring_list.append(each_char)
                else:
                    substring_list[-1]=substring_list[-1]+each_char
        return len(substring_list)
            