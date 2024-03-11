"""
Date: March 11, 2024
Name: Rajashree Dahal
Problem:
You are given two 0-indexed integer arrays jobs and workers of equal length, where jobs[i] is the amount of time needed to complete the ith job, and workers[j] is the amount of time the jth worker can work each day.
Each job should be assigned to exactly one worker, such that each worker completes exactly one job.
Return the minimum number of days needed to complete all the jobs after assignment.
"""
import math
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        workers=sorted(workers)
        jobs=sorted(jobs)
        timeList=[math.ceil(j/i) for i, j in zip(workers,jobs)]
        return max(timeList)