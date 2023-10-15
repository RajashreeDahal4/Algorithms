'''
Date: October 14, 2023
Name: Rajashree Dahal
Problem: Max Numbe of K-Sum Pairs
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose 
sum equals k and remove them from the array.Return the maximum number of operations you can perform on the array.
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_dict={}
        max_count=0
        #forming a dictionary that keeps track of count of each element in the list
        for i in nums:
            if i not in count_dict.keys():
                count_dict[i]=1
            else:
                count_dict[i]=count_dict[i]+1
        for i in nums:
            if i in count_dict.keys() and count_dict[i]>0:
                remaining=k-i
                count_dict[i]=count_dict[i]-1
                if remaining in count_dict.keys() and count_dict[remaining]>0:
                    max_count=max_count+1
                    count_dict[remaining]=count_dict[remaining]-1
                else:
                    count_dict[i]=count_dict[i]+1
        return max_count

