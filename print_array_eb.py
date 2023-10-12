'''
Date: October 11, 2023
Name: Rajashree Dahal
Problem: Write a recursive/nonrecursive/d&c algorithm to print an array from the end to the beginning.
'''

def non_recursive_print(array):
    final_array=[]
    length=len(array)
    for i in range(len(array)):
        final_array.append(array[length-1-i])
    print(final_array)


non_recursive_print(array=[1,2,3,4,5])


def recursive_print(array,final_array):
    if len(array)==len(final_array):
        return final_array 
    else:
        
