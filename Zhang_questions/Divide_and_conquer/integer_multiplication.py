"""
Date: October 14, 2023
Name: Rajashree Dahal
Problem: 
        You are given two integers, "a" and "b," and you need to find their product using a divide and 
        conquer algorithm. The goal is to efficiently compute the product of these integers by breaking 
        down the problem into smaller sub-problems and recursively solving them.
"""

def integer_multiplication(num1,num2):
    if num1<10 or num2<10:
        return num1*num2
    else:
        num1_str=str(num1)
        num2_str=str(num2)
        n=max(len(num1_str),len(num2_str))
        # Split the numbers into two parts
        m = n // 2
        a1 = num1 // 10**m
        a0 = num1 % 10**m
        b1 = num2 // 10**m
        b0 = num2 % 10**m
        bd=integer_multiplication(a0,b0)
        ac=integer_multiplication(a1,b1)
        ac_bd=integer_multiplication(a1,b0)+integer_multiplication(a0,b1)
        result = (ac * 10**(2 * m)) + (ac_bd * 10**m) + bd
        return result
    
product=integer_multiplication(256,256)
print(product)