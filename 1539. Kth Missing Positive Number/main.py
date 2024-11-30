class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count=0
        count2=0
        count3=0
        for i in range(1,max(arr)):
            if(i==arr[count3]):
                count3+=1
            else:
                count2+=1
            if(count2==k):
                return i
        j=max(arr)
        while True:
            j+=1
            count2+=1
            if(count2==k):
                return j
            
       
        
