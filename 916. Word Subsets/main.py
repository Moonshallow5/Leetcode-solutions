class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
       
        
        res=""
        maxFreq=Counter()
        for word in words2:
            wordFreq=Counter(word)
            for char,value in wordFreq.items():
                maxFreq[char]=max(value,maxFreq[char])
        print(maxFreq)

        res2=[]
        for word in words1:
            count2=Counter(word)
            if all(count2[char]>=maxFreq[char] for char in maxFreq):
                res2.append(word)
        return res2


        
