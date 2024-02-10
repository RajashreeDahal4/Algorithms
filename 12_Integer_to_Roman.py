"""
Date: February 10, 2024
Name: Rajashree Dahal
Problem:Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""
class Solution:
    def intToRoman(self, num: int,result=None) -> str:
        if result is None:
            result=""
        hash={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",
        9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        if num in hash:
            return result+hash[num]
        if num>1000:
            result =self.intToRoman(num-1000,result+hash[1000])
        elif num>900:
            result =self.intToRoman(num-900,result+hash[900])
        elif num>500:
            result=self.intToRoman(num-500,result+hash[500])
        elif num>400:
            result=self.intToRoman(num-400,result+hash[400])
        elif num>100:
            result=self.intToRoman(num-100,result+hash[100])
        elif num>90:
            result=self.intToRoman(num-90,result+hash[90])
        elif num>50:
            result=self.intToRoman(num-50,result+hash[50])
        elif num>40:
            result=self.intToRoman(num-40,result+hash[40])
        elif num>10:
            result=self.intToRoman(num-10,result+"X")
        elif num>9:
            result=self.intToRoman(num-9,result+hash[9])
        elif num>5:
            result=self.intToRoman(num-5,result+hash[5])
        elif num>4:
            result=self.intToRoman(num-4,result+hash[4])
        elif num>1:
            result=self.intToRoman(num-1,result+hash[1])
        return result