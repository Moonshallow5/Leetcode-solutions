class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        maxi=0
        res=[]
        count=0
        l=0
        for i in range(len(s)):
            if(s[i] in vowels):
                count+=1
            if(i-l+1>k):
                if(s[l] in vowels):
                    count-=1
                l+=1
            maxi=max(maxi,count)
                
        return maxi
            
            
    


        
