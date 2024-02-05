"""
Date: February 5, 2024
Name: Rajashree Dahal
Problem: Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)==set(word2):
            if sorted(Counter(word1).values())==sorted(Counter(word2).values()):
                return True
        else:
            return False
