"""
Date: February 28, 2024
Name: Rajashree Dahal
Problem:Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.issimilar(root.left,root.right)
        
    def issimilar(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val!=right.val:
            return False
        return self.issimilar(left.left,right.right) and self.issimilar(left.right,right.left)
