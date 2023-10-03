'''
Date: October 2, 2023
Name: Rajashree Dahal
Problem:
You are given all numbers between 1 and n but there is one number missing.
Your task is to write a program to find and print the missing number. The
program will accept input on two lines, the first line will accept the value of n
and the second line will accept n−1 numbers, each between 1 and n. The output
of the program will be the missing number. Note that the program should run
in under 1 s.
Input:
10
1 2 3 4 5 6 7 8 10
Output:
9
''' 
import time
def missing_number(n,numbers):
    start_time=time.time()
    expected_sum=int(n*(n+1)/2)
    given_numbers_sum=sum(numbers)
    missing_number=expected_sum-given_numbers_sum
    print("The time taken for execution is",time.time()-start_time)
    return missing_number

# Input
print("Please enter an integer value of n:")
n = int(input())
print("Please enter the values from 1 to n with one number missing.All numbers should be separated by single space")
numbers = list(map(int, input().split()))
missing_number=missing_number(n,numbers)
print("The missing Number is",missing_number)
