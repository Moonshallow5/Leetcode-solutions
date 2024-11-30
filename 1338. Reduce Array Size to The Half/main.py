class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        count2=dict(count.most_common())

        n=len(arr)//2
        sums=0
        maxi=float('inf')
        res=[]

        for key,val in count2.items():
            res.append(key)
            sums+=val

            if(sums>=n):
                maxi=min(maxi,len(res))
                res=[]
                sums=0
        return maxi
