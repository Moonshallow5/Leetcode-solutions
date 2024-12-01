class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic={}
        for i,j in enumerate(arr):
            if(2*arr[i] in dic or ((arr[i]/2 in dic and arr[i]%2==0))):
                return True
                
            else:
                dic[j]=i
        return False
        
