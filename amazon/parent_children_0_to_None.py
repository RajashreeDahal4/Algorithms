"""
Date: February 28, 2024
Name:Rajashree Dahal
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def set_zero_subtrees_to_none(root):
    if not root:
        return None
    
    # Recursively set zero subtrees to None
    root.left = set_zero_subtrees_to_none(root.left)
    root.right = set_zero_subtrees_to_none(root.right)
    
    # If the current node and its children are all zeros, set the node value to None
    if not root.val and not root.left and not root.right:
        return None
    
    return root

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(2)
root.right.right = TreeNode(2)
root.left.right.right = TreeNode(0)

# Function to print the tree
def print_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_tree(root.left)
    print_tree(root.right)

print("Original Binary Tree:")
print_tree(root)
print("\n")

# Set zero subtrees to None
root = set_zero_subtrees_to_none(root)

# Print modified binary tree
print("Binary Tree after setting zero subtrees to None:")
print_tree(root)