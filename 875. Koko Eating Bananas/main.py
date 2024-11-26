class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        r=max(piles)
       
        res=r

        while(l<=r):
            mid=l+(r-l)//2
            totaltime=0
            for i in piles:
                totaltime+=math.ceil((float(i)/mid))
            
            if(totaltime>h):
                l=mid+1
            else:
                res=min(res,mid)
                r=mid-1
                
        return res
