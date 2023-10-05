"""
Date: October 4, 2023
Name: Rajashree Dahal
Problem: 3: Design a linear-time recursive algorithm, in pseudo-code to evaluate the  polynomial anxn+an-1xn-1+...a1x+a0.  
Note that, ais are given, x is the variable. (20pts)
"""
import math
def polynomial_evaluation(x,a_values,start,end,dummy):
    '''
    a_values: contain list of a values from 0 to n
    dummy: keeps track of index position of a_values splitted across different recursion
    '''
    if len(a_values)==1:
        return (a_values[0]*math.pow(x,dummy[0]))
    num_terms=len(a_values)
    mid_term=int(num_terms/2)
    left_sum=polynomial_evaluation(x,a_values[0:mid_term],start,mid_term,dummy[0:mid_term])
    right_sum=polynomial_evaluation(x,a_values[mid_term:],mid_term,end,dummy[mid_term:])
    final_sum=left_sum+right_sum
    return final_sum

a_values=[1,1,1,1,1,1,2]
result=polynomial_evaluation(6,a_values,0,2,[i for i in range(len(a_values))])
print(result)