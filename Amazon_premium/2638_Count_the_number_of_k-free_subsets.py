"""
Date: March 10, 2024
Name: Rajashree Dahal
Problem: 
You are given an integer array nums, which contains distinct elements and an integer k.
A subset is called a k-Free subset if it contains no two elements with an absolute difference equal to k. Notice that the empty set is a k-Free subset.
Return the number of k-Free subsets of nums.
A subset of an array is a selection of elements (possibly none) of the array.
"""
class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        def fact(s,k):
            for num in s:
                if (num - k) in s or (num + k) in s:
                    return False
            return True

        def search(m,nums):
            if m == (len(nums)):
                # print(set(subset))
                if subset:
                    result_=fact(set(subset),k)
                    if result_:
                        final_result.append(set(subset))
                else:
                    final_result.append({})
                pass
            else:
                subset.append(nums[m])
                search(m + 1,nums)
                subset.pop()
                # Don't include k in the subset
                search(m + 1,nums)
        subset=[]
        final_result=[]
        search(0,nums)
        return len(final_result)
