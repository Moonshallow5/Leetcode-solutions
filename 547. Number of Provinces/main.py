class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit=[False]*len(isConnected)

        def dfs(city):
            visit[city]=True
            for i,v in enumerate(isConnected[city]):

                if(not visit[i] and v):
                    dfs(i)

        count=0
        for city in range(len(isConnected)):
            if not visit[city]:
                dfs(city)
                count+=1
        return count
