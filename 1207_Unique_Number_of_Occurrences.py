"""
Date: February 5, 2024
Name: Rajashree Dahal
Problem: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict={}
        for each_element in arr:
            if each_element in count_dict:
                count_dict[each_element]=count_dict[each_element]+1
            else:
                count_dict[each_element]=1
        if len(count_dict)==len(set(count_dict.values())):
            return True
        else:
            return False