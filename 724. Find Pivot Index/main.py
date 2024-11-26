class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum,rightsum=0,sum(nums)
        for i,v in enumerate(nums):
            rightsum-=v
            if(leftsum==rightsum):
                return i
            leftsum+=v
        return -1
        
