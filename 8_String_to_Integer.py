"""
Date: February 10, 2024
Name: Rajashree Dahal
Problem:Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The algorithm for myAtoi(string s) is as follows:
Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        for each_char in s:
            if each_char not in ["+","-"," "]:
                sign=False
                break
            else:
                if each_char==" ":
                    s=s.lstrip()
                if each_char=="+":
                    sign=False
                    s=s.replace("+","",1)
                    break
                elif each_char=="-":
                    sign=True
                    s=s.replace("-","",1)
                    break
                else:
                    sign=False
        values_read=[1,2,3,4,5,6,7,8,9,0]
        values_read=[str(i) for i in values_read]
        result=""
        for i in s:
            if i in values_read:
                result=result+i
            else:
                break
        if result:
            result=int(result)
            result=-1*result if sign else result
            if result<(-2**31) or result>(2**31-1):
                result= -2**31 if result<(2**31-1) else (2**31-1)
                return result
            else:
                return result

        return 0