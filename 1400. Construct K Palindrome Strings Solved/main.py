class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if(k>len(s)):
            return False
        counter=Counter(s)
        res=0

        for i in counter.values():
            if(i%2!=0):
                res+=1
        return res<=k

        
