class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i,j=0,len(costs)-1
        h1=[]
        h2=[]
        res=[]
        while(len(res)<k):
            while(len(h1)<candidates and i<=j):
                heapq.heappush(h1,(costs[i],i))
                i+=1
            while(len(h2)<candidates and i<=j):
                heapq.heappush(h2,(costs[j],j))
                j-=1
            if h1 and h2:
                if(h1[0][0]<=h2[0][0]):
                    val=heapq.heappop(h1)
                else:
                    val=heapq.heappop(h2)
            elif h1:
                val=heapq.heappop(h1)
            
            elif h2:
                val=heapq.heappop(h2)
            res.append(val[0])
        return sum(res)
