'''
Date: September 25, 2023
Name: Rajashree Dahal
Problem Statement:
Given an array or sequence of elements, the task is to count the number of inversions in that array. In other words, you need to determine how many pairs of elements are in an inverted order compared to their sorted order.
Mathematically, you are looking for the count of pairs (i, j) where 0 <= i < j < n (n is the length of the array), and arr[i] > arr[j].
'''
sort_arr=[]
def count_inversions(arr):
    if len(arr)==1:
        return arr,0
    else:
        mid=len(arr)//2
        #Implementing divide and conquer approach here
        left_arr,left_inv_count=count_inversions(arr[:mid])
        right_arr,right_inv_count=count_inversions(arr[mid:])
        i,j=0,0
        inv_count=0
        sort_arr=[]
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]>right_arr[j]:
                inv_count=inv_count+len(left_arr[i:len(left_arr)])
                sort_arr.append(right_arr[j])
                j=j+1
            else:
                sort_arr.append(left_arr[i])
                i=i+1
        sort_arr.extend(left_arr[i:len(left_arr)])
        sort_arr.extend(right_arr[j:len(right_arr)])
        inv_count=inv_count+left_inv_count+right_inv_count
    return sort_arr,inv_count



arr,inv_count=count_inversions([3,4,2,3,4,5,3])
print(arr,inv_count)
# print((0+8)//2)
# arr=[3,4,2,1,0,9,15,16]
# print(arr[3+1:])





# def count_inversion(given_array,i,j):
