"""
Date: February 28, 2024
Name: Rajashree Dahal
Problem:
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        #trying to make max heap out of it
        stones=[-1*i for i in stones]
        heapq.heapify(stones)
        print(stones)
        while stones:
            s1=-1*heappop(stones)
            if not stones:
                return s1
            s2=-heappop(stones)
            if s1>s2:
                heappush(stones,s2-s1)
        return 0