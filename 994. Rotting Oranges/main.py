class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q=deque()
        fresh=0
        time=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c]==1):
                    fresh+=1
                elif(grid[r][c]==2):
                    q.append((r,c))
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if(row in range(len(grid)) and col in range(len(grid[0]))):
                        if(grid[row][col]==1):
                            grid[row][col]=2
                            fresh-=1
                            q.append((row,col))
            time+=1
        if(fresh==0):
            return time
        return -1
            
        
