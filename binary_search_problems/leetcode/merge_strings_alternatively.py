'''
Date: October 10, 2023
Name: Rajashree Dahal
Problem:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final_length=len(word1)+len(word2)
        word=""
        counter1,counter2=0,0
        start=0
        for i in range(final_length):
            if start==0 and counter2==len(word2):
                word=word+word1[counter1:]
                return word 
            elif start==1 and counter1==len(word1):
                word=word+word2[counter2:]
                return word
            elif (counter1<len(word1) and start==0 and (counter2<len(word2))):
                word=word+word1[counter1]
                counter1=counter1+1
                start=1
            elif counter2<len(word2) and start==1:
                word=word+word2[counter2]
                counter2=counter2+1
                start=0
        return word
