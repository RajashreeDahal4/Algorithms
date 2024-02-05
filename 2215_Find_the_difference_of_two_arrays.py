"""
Date: February 5, 2024
Name: Rajashree Dahal
Problem:Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order. 
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        only_nums1=list(set(nums1)-set(nums2))
        only_nums2=list(set(nums2)-set(nums1))
        return[only_nums1,only_nums2]