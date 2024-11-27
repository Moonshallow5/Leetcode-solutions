class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        x=heapq.heapify(nums)
        n=len(nums)
        res=[]
        for i in range(n):
            res.append(heapq.heappop(nums))
        return res

        
        
