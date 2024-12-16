class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res=[]
        for i,v in enumerate(nums):
            heapq.heappush(res,(v,i))
        print(res)
        while k!=0:
            (v,i)=heapq.heappop(res)
            v*=multiplier
            heapq.heappush(res,(v,i))
            k-=1
        print(res)
        while res:
            (v,i)=heapq.heappop(res)
            nums[i]=v
        return nums
            

        return []

        
