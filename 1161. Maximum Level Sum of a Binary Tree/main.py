# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=deque()
        sums=0
        count=1
        sumi=0
        res=[]
        if root:
            q.append(root)
            res.append(root.val)
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if(node.left):
                    sums+=node.left.val
                    q.append(node.left)
                if(node.right):
                    sums+=node.right.val
                    q.append(node.right)
                
            res.append(sums)
            sums=0
            count+=1
        print(res)
        res.pop()
        print(res)

        x=max(res)
        return res.index(x)+1

        

                
        
