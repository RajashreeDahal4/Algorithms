"""
Date: February 5, 2024
Name: Rajashree Dahal
Problem: Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_array=np.array(grid)
        grid=[str(i) for i in grid]
        grid_count={}
        for each_grid in grid:
            if each_grid not in grid_count:
                grid_count[each_grid]=1
            else:
                grid_count[each_grid]=grid_count[each_grid]+1

        transpose_grid_array=grid_array.transpose()
        transpose=[str(list(i)) for i in transpose_grid_array]
        result=0
        for each_array in transpose:
            if each_array in grid_count:
                count=grid_count[each_array]
                while count>0:
                    result=result+1
                    count=count-1
        return result
