# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if self.prev is not None:
                self.min_diff=min(self.min_diff,abs(node.val-self.prev))
            self.prev=node.val
            in_order(node.right)
            
        self.prev=None
        self.min_diff=10**10
        in_order(root)
        return self.min_diff
        
