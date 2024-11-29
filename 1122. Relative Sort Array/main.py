class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)
        res=[]

        for i in arr2:
            if i in count:
                res.extend([i]*count[i])
                del count[i]
        res2=[]
        
        for i,z in count.items():
            res2.extend([i]*z)
        res2.sort()

        res=res+res2
    
        return res
