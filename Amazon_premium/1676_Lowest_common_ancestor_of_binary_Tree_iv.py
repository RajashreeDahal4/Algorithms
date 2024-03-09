"""
Date: March 9, 2024
Name: Rajashree Dahal
Problem:
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for e
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
     def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not root:
            return None
        
        def helper(node):
            if not node:
                return None
            
            if node in nodes:
                return node
            
            left = helper(node.left)
            right = helper(node.right)
            
            if left and right:
                return node
            
            return left if left else right
        
        return helper(root)