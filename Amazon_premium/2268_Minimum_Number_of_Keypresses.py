"""
Date: March 10, 2024
Name: Rajashree Dahal
Problem:
You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:
All 26 lowercase English letters are mapped to.
Each character is mapped to by exactly 1 button.
Each button maps to at most 3 characters.
To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.
Given a string s, return the minimum number of keypresses needed to type s using your keypad.
Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.
"""
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count_dict=Counter(s)
        sorted_values=sorted(count_dict.values(),reverse=True)
        key_presses=0
        total_presses=0
        dist_map=0
        factor=1
        for multiplier in sorted_values:
            total_presses=total_presses+multiplier*factor
            dist_map=dist_map+1
            if dist_map%9==0:
                factor=factor+1
        return total_presses

        