class Solution:
    def findScore(self, nums: List[int]) -> int:
        min_heap=[(val,idx) for idx,val in enumerate(nums)]
        count=0

        heapq.heapify(min_heap)
        while min_heap:
            val,idx=heapq.heappop(min_heap)
           
            if(nums[idx]!=-1):
                count+=val
                nums[idx]=-1
                if(idx>0 and nums[idx-1]!=-1):
                    nums[idx-1]=-1
                if(idx<len(nums)-1 and nums[idx+1]!=-1):
                    nums[idx+1]=-1
        return count
            

        
