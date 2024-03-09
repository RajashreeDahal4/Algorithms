"""
Date: March 9, 2024
Name: Rajashree Dahal
Problem: Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
"""
class Solution:
    def minSwaps(self, data: List[int]) -> int:
            one_count = sum(data)
            if one_count <= 1:
                return 0

            window_size = one_count
            # Initialize the count of 1's in the first window
            current_count = sum(data[:window_size])
            max_count = current_count

            # Slide the window and update max_count
            for i in range(1, len(data) - window_size + 1):
                # Update count of 1's for the current window
                current_count = current_count - data[i - 1] + data[i + window_size - 1]
                max_count = max(max_count, current_count)

            # Calculate the minimum swaps required
            min_swaps = one_count - max_count
            return min_swaps
        