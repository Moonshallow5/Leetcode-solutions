class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        intervals.sort()
        for interval in intervals:
            if(newInterval[1]<interval[0]):
                res.append(newInterval)
                newInterval=interval
            elif(newInterval[0]>interval[1]):
                res.append(interval)
            else:
                newInterval[0]=min(newInterval[0],interval[0])
                newInterval[1]=max(newInterval[1],interval[1])
        res.append(newInterval)
            
        
        return res

        
