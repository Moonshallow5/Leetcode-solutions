class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i,j=0,len(citations)
        count=0
        citations.sort(reverse=True)

        while(i<j):
            mid=i+(j-i)//2
            count=0
        
            if(citations[mid]>=mid+1):
                i=mid+1
            else:
                j=mid
            
        return i
        
