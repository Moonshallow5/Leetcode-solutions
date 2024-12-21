class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums)
        print(res)
        heap=[]
        res2=[]
        for key,val in res.items():
            heapq.heappush(heap,(-val,key))
        while k!=0:
            x,y=heapq.heappop(heap)
            res2.append(y)
            k-=1
        return res2
        


        
