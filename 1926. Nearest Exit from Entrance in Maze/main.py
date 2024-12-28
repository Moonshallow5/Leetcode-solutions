class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS=len(maze)
        COLS=len(maze[0])
        q=deque([(entrance[0],entrance[1],0)])
        maze[entrance[0]][entrance[1]]='+'
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            row,col,steps=q.popleft()
            for dr,dc in directions:
                r,c=row+dr,col+dc
                if(r>=0 and r<ROWS and c>=0 and c<COLS and maze[r][c] =='.'):
                    if((r==ROWS-1 or r==0) or (c==COLS-1 or c==0) ):
                        return steps+1
                    maze[r][c]='+'
                    q.append((r,c,steps+1))
        return -1


                
            
            

        
        
