class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q=deque([(0,0,0)])
        visit=set()
        visit.add((0,0))
        m,n=len(grid),len(grid[0])

        directions=[(0,-1),(0,1),(1,0),(-1,0)]

        while q:
            x,y,obstacles=q.popleft()
            if(x==len(grid)-1 and y==len(grid[0])-1):
                return obstacles
            for dx,dy in directions:
                row,col=x+dx,y+dy
                if(0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in visit):
                    visit.add((row,col))
                    if(grid[row][col]==0):
                        q.appendleft((row,col,obstacles))
                    else:
                        q.append((row,col,obstacles+1))
        return -1

            

        
