class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT,window={},{}
        for r in t:
            countT[r]=1+countT.get(r,0)
        print(countT)

        have,need=0,len(countT)
        res,resLen=[-1,-1],float('inf')
        l=0

        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            if(s[r] in countT and window[s[r]]==countT[s[r]]):
                have+=1
            while have==need:
                if(r-l+1)<resLen:
                    resLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if(s[l] in countT and window[s[l]]<countT[s[l]]):
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float('inf') else ""

        
