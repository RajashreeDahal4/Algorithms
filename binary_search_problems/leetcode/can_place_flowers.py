'''
Date: October 11, 2023
Name: Rajashree Dahal
Problem:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count,i=0,0
        if n==0:
            return True
        while i<len(flowerbed):
            if flowerbed[i]==0:
                if (i==len(flowerbed)-1) or flowerbed[i+1]==0:
                    if (i-1)<0:
                        flowerbed[i]=1
                        count=count+1
                    elif flowerbed[i-1]==0:
                        flowerbed[i]=1
                        count=count+1
            if count==n:
                return True
            i=i+1
        return False