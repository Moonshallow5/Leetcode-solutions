class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=max(candies)
        res=[]
        for i in candies:
            if(i+extraCandies>=n):
                res.append(True)
            else:
                res.append(False)
        return res

        
