"""
Date: January 31, 2024
Name: Rajashree Dahal
Problem: Given an array of integers nums sorted in non-decreasing order, find the starting and ending 
position of a given target value. If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexes=[]
        if target not in nums:
            return [-1,-1]
        elif len(nums)==1 and nums[0]==target:
            return [0,0]
        else:
            start=0
            end=len(nums)
            mid=int((start+end)/2)
            while True:
                if nums[mid]==target:
                    real_mid=mid
                    while nums[mid]==target:
                        indexes.append(mid)
                        if mid>=1:
                            mid=mid-1
                        else:
                            break
                    print("mid",mid)
                    print("real mid",real_mid)
                    while nums[real_mid]==target:
                        indexes.append(real_mid)
                        real_mid=real_mid+1
                        if real_mid>=len(nums):
                            break
                    return [min(indexes),max(indexes)]
                elif nums[mid]<target:
                    start=mid
                    mid=int((start+end)/2)
                else:
                    end=mid
                    mid=int((start+end)/2)
