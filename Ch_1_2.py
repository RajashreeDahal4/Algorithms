"""
Date: December 14, 2023
Name: Rajashree Dahal
Problem: Write code to reverse a C-Style String. (C-string means that "abcd" is represented as five characters, including
the null characters)
"""

def reverse_C_string(string):
    len_string=len(string)-1
    reverse_string=""
    for i in range(1,len(string)):
        index=len_string-i
        reverse_string=reverse_string+string[index]
    reverse_string=reverse_string+string[-1]
    return reverse_string

