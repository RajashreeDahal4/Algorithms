"""
Date: January 28, 2024
Name: Rajashree Dahal
Project:Given a string s containing just the characters '(', ')',
 '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        result = [] 
        for c in s: 
            if c in '([{': 
                result.append(c) 
            else: 
                if not result or (c == ')' and result[-1] != '(') or \
                    (c == '}' and result[-1] != '{') or \
                    (c == ']' and result[-1] != '['):
                    return False 
                result.pop() 
        return not result 