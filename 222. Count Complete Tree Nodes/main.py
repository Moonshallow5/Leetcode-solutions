# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q=deque()
        count=0
        if root:
            q.append(root)
            count+=1
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                    count+=1
                if(node.right):
                    q.append(node.right)
                    count+=1
        return count
        
