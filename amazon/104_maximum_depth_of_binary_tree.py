"""
Date: February 28, 2024
Name: Rajashree Dahal
Problem: Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode],depth=0) -> int:
        if root is None:
            return depth
        depth=depth+1
        left_depth=self.maxDepth(root.left,depth)
        right_depth=self.maxDepth(root.right,depth)
        max_depth=max(left_depth,right_depth)
        return max_depth
        