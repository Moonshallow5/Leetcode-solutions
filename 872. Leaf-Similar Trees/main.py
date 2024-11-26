# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool


        """
        def leaves(root):
            s1 = deque()
            leaf = []
            s1.append(root)

            while s1:
                for i in range(len(s1)):
                    curr = s1.pop()
                    if curr.left:
                        s1.append(curr.left)
                    if curr.right:
                        s1.append(curr.right)
                    if not curr.left and not curr.right:
                        leaf.append(curr.val)
            return leaf

        return leaves(root1) == leaves(root2)
            
