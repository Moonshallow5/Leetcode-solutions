class Solution:
    import math
    def pickGifts(self, gifts: List[int], k: int) -> int:
        min_heap=[-i for i in gifts]
        print(min_heap)
        heapq.heapify(min_heap)
        while k>0:
            x=math.floor(math.sqrt(-heapq.heappop(min_heap)))
            heapq.heappush(min_heap,-x)
            k-=1
       
        return -sum(min_heap)


        
