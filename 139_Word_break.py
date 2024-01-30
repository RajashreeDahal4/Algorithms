"""
Date: January 29, 2024
Name: Rajashree Dahal
Problem: Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.Note that the same word in the dictionary may be reused multiple times in 
the segmentation.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        wordDict.reverse()
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if s[i - len(w) : i] == w and dp[i - len(w)]:
                    dp[i] = True
                    break
        return dp[-1]