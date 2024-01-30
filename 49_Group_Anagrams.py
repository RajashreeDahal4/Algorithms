"""
Date: January 29, 2024
Name: Rajashree Dahal
Problem:Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_string=[''.join(sorted(my_string)) for my_string in strs]
        anagram={}
        for enum,i in enumerate(sorted_string):
            if i not in anagram.keys():
                anagram[i]=[enum]
            else:
                value=anagram[i]
                value.append(enum)
                anagram[i]=value
        anagram_groups=[[strs[index] for index in value]for key,value in anagram.items()]
        return anagram_groups
