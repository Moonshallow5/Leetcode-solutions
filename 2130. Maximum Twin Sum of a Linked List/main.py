# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        stack=[]
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        while slow:
            stack.append(slow.val)
            slow=slow.next
        x=head
        sumi=0
        res=0
        while stack:
            sumi=x.val+stack.pop()
            res=max(res,sumi)
            x=x.next
        return res
        


        
