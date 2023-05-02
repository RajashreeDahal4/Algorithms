'''
Search in a bitonic array. An array is bitonic if it is comprised of an increasing sequence of 
integers followed immediately by a decreasing sequence of integers. Write a program that, 
given a bitonic array of n distinct integer values, determines whether a given integer is in the array.
Standard version: use ~ 3lg n compares in the worst case
Signing bonus ~ use ~2lgn compares in the worst case (and prove that no algorithm can guarantee to perform fewer than ~2lg n compares in the worst case)

'''
import numpy as np
first_array=np.array([7,8,9,10,11,12,13,14,6,5,4,3,2,1])

def find_integer_exists(num,first_array):
    n=len(first_array)
    left,right=0,n-1
    #find the maximum value in the array
    count=1
    while(left<right):
        #this loop takes logN time to find the max value in the array
        mid_point=int((left+right)/2)
        if first_array[mid_point]<first_array[mid_point+1]:
            left=mid_point+1
        else:
            right=mid_point
    peak=first_array[mid_point]
    peak_position=mid_point
    left,right=0,mid_point
    #now searching for the target in the left half using binary search
        #going to left half
    left,right=0,peak_position
    while (left<=right):
        mid_point=int((left+right)/2)
        if (first_array[mid_point]==num or first_array[left]==num or first_array[right]==num):
            print("The target exists in the array")
            return 1
        elif first_array[mid_point]>num:
            right=mid_point-1
        else:
            left=mid_point

    #goint to right half
    left,right=peak_position,n-1
    while (left<=right):
        mid_point=int((left+right)/2)
        if first_array[mid_point]==num:
            print("The target exists in the array")
            return 1
        elif first_array[mid_point]>num:
            left=mid_point+1
        else:
            right=mid_point
    print("the number doesnot exist in the array")

find_integer_exists(14,first_array)
