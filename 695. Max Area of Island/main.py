class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        area=0

        def dfs(r,c):
            if(r>=row or r<0 or c>=col or c<0 or grid[r][c]!=1 or (r,c) in visit ):
                return 0
            visit.add((r,c))
            return (1+dfs(r,c+1)+dfs(r,c-1)+dfs(r-1,c)+dfs(r+1,c))
        for r in range(row):
            for c in range(col):
                area=max(dfs(r,c),area)
        return area
