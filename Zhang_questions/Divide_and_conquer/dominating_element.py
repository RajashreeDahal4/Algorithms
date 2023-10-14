"""
Date: October 14, 2023
Name: Rajashree Dahal
Problem Statement: Dominating Element Identification Using Divide and Conquer
You are given an array of integers, and your task is to identify a dominating element, if one exists. A dominating element is an element that appears more than half of the time in the array.
Input:
An array of integers, arr, containing n (1 <= n <= 10^6) elements.
Each element in the array is an integer within the range [-10^9, 10^9].
Output:
If a dominating element exists, return that element.
If no dominating element is found, return "No dominating element."
"""
def dominating_element(array,start,end):
    if len(array)==1:
        return array[0]
    if start==end:
        return array[start]    
    else:
        mid=(start+end)//2
        left_dominating_element=dominating_element(array,start,mid)
        right_dominating_element=dominating_element(array,mid+1,end)
        count_left,count_right=0,0
        for i in range(start,end+1):
            if (left_dominating_element==array[i]):
                count_left=count_left+1
            if (right_dominating_element==array[i]):
                count_right=count_right+1
        if (count_left>(end-start)//2):
            return left_dominating_element
        elif (count_right>(end-start)//2):
            return right_dominating_element
        else:
            return None
            

        
element=dominating_element([2,4,2,3,2,0,2],0,6)
print(element)