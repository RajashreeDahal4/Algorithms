"""
Date: March 10, 2024
Name: Rajashree Dahal
Problem:
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, a: 'Node', b: 'Node') -> 'Node':
        ancestors = set()
        while a is not None:
            ancestors.add(a)
            a = a.parent
            
        while b is not None:
            if b in ancestors:
                return b
            b = b.parent