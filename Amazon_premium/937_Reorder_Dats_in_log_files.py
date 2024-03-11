"""
Date: March 11, 2024
Name: Rajashree Dahal
Problem:
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:
Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sorting_algorithm(log):
			# Is a numerical log, make sure these entries appear on the right side without further sorting.
            if log[-1].isnumeric():
				# A tuple of one element. One element tuples need a trailing comma so they are not confused with a simple one (1) or 1 by python.
                return (1,)
            left_side, right_side = log.split(" ", 1)
            return (0, right_side, left_side)
        return sorted(logs, key=sorting_algorithm)

