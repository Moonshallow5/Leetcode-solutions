# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_nodes(nodes,target):
            if not nodes:
                return 0
            count=0
            if target==nodes.val:
                count+=1
            count+=count_nodes(nodes.left,target-nodes.val)
            count+=count_nodes(nodes.right,target-nodes.val)

            return count
        if not root:
            return 0
        count=count_nodes(root,targetSum)
        count+=self.pathSum(root.left,targetSum)
        count+=self.pathSum(root.right,targetSum)
        return count



