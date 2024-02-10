"""
Date: February 10, 2024
Name: Rajashree Dahal
Problem: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution:
    def letterCombinations(self, digits: str, dict_map=None, combination=None, result=None) -> List[str]:
            if dict_map is None:
                dict_map = {"": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
            if result is None:
                result = []
            if combination is None:
                combination = ""

            if not digits:
                return result

            if len(combination) == len(digits):
                result.append(combination)
                return result

            index = digits[len(combination)]
            word = dict_map[index]

            for each_char in word:
                result = self.letterCombinations(digits, dict_map, combination + each_char, result)

            return result