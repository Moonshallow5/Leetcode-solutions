class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]

        def dfs(i,curr,total):
            if(len(curr)==k):
                if(total==0):
                    res.append(curr)
                return
            for num in range(i+1,10):
                if(num<=total):
                    dfs(num,curr+[num],total-num)
                else:
                    return
        dfs(0,[],n)
        return res
            
                

        
