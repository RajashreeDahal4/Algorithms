"""
Dahal: February 28, 2024
Name: Rajashree Dahal
Problem:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,low,high):
            if not node:
                return True
            result=low<node.val<high
            return result and dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
        return dfs(root,float('-inf'),float('inf'))
        