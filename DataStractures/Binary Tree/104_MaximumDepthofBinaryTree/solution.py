# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: list[TreeNode]) -> int:
        # base case: if the root is None, return 0
        if root is None:
            return 0

        # recursive case: return the maximum of the depth of the left and right subtrees plus 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
