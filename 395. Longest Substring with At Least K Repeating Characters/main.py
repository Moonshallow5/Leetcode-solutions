class Solution:
    def longestSubstring(self, s: str, k: int) -> int:


        freq=Counter(s)

        for i in freq:
            if(freq[i]<k):
                return max(self.longestSubstring(sub,k) for sub in s.split(i))
        return len(s)


   
        
