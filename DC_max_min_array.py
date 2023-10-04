'''
Date: October 3, 2023
Name: Rajashree Dahal
Problem Statement:
Design a divide-and-conquer algorithm, in pseudo-code to compute the maximum and the minimum of a given array A. 
'''

def max_min(array_list):
    print(array_list)
    if len(array_list)==1:
        return array_list[0],array_list[0]
    else:
        mid=int(len(array_list)/2)
        left_min,left_max=max_min(array_list[0:mid])
        right_min,right_max=max_min(array_list[mid:])
        
        max_num,min_num=0,0
        if left_max<right_max:
            max_num=right_max
        else:
            max_num=left_max
        if left_min<=right_min:
            min_num=left_min
        else:
            min_num=right_min
        return min_num,max_num
        
# Test the function
array = [3, 7, 1, 9, 4, 6, 8, 2]
min_val, max_val = max_min(array)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")





