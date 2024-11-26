# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        while True:
            if(root and root.val>val):
                root=root.left
            elif(root and root.val<val):
                root=root.right
            else:
                return root
        return None
        
        
        
        
