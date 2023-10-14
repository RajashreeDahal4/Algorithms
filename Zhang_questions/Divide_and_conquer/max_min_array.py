'''
Date: October 14, 2023
Name: Rajashree Dahal
Problem: Find the max and min of an array using divide and conquer algorithm
'''

def max_min_array(array,start,end):
    if start==end:
        return array[start],array[start]
    else:
        mid=(start+end)//2
        left_max,left_min=max_min_array(array,start,mid)
        right_max,right_min=max_min_array(array,mid+1,end)
        if left_max>right_max:
            maximum=left_max
        else:
            maximum=right_max
        if left_min<right_min:
            minimum=left_min 
        else:
            minimum=right_min 
    return maximum,minimum 
results=max_min_array([4,1,2,6,100,-10,0],0,6)
print(results)