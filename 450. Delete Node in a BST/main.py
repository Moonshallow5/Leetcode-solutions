# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if(not root):
            return None
        elif(root.val>key):
            root.left=self.deleteNode(root.left,key)
            return root     
        elif(root.val<key):
            root.right=self.deleteNode(root.right,key)
            return root
    
        else:
            if(root.left is None):
                return root.right
            if(root.right is None):
                return root.left
            x=root.right
            while(x.left):
                x=x.left
            root.val=x.val
            root.right=self.deleteNode(root.right,x.val)
            return root

            
