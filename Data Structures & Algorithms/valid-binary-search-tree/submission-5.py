# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, leftVal, rightVal):
            if not node:
                return True
            if node.val >= rightVal or node.val <= leftVal:
                return False

            return valid(node.left, leftVal, node.val) and valid(node.right, node.val, rightVal)

        return valid(root, float("-inf"), float("inf"))
