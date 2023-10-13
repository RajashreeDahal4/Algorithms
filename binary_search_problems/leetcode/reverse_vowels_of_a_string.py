'''
Date: October 12, 2023
Name: Rajashree Dahal
Probelm:  Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        Target: Reverse Vowels of a string 
        '''
        target="aeiouAEIOU"
        original_index=[enum for enum,i in enumerate(s) if i in target ]
        original_vowels=[i for i in s if i in target ]
        if len(original_index)>1:
            reversed_vowel_string=""
            start_index=0
            len_vowels=len(original_vowels)-1
            for i in range(len(original_index)):
                reversed_vowel_string+=s[start_index:original_index[i]]
                reversed_vowel_string+=original_vowels[len_vowels-i]
                start_index=original_index[i]+1
            return reversed_vowel_string+s[original_index[-1]+1:]
        else:
            return s