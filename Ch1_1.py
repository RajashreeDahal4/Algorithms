"""
Date: December 14, 2024
Name: Rajashree Dahal
Problem: Implement an algorithm to determine if a string has all unique characters
"""

def unique_characters(string):  #Time complexity of the problem: O(n)
    result=True
    char_dict={}  #This is used to keep track of characters in the string
    for each_character in string:
        if each_character in char_dict:
            result=False
            return result 
        else:
            char_dict[each_character]=True
    return result 

