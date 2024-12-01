class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix=[[0 for _ in range(n)] for _ in range(m)]
        print(matrix)
        for i in range(len(indices)):
            index_row=indices[i][0]
            index_col=indices[i][1]

            for j in range(n):
                matrix[index_row][j]+=1

            for k in range(m):
                matrix[k][index_col]+=1
        cnt=0
        for r in range(m):
            for c in range(n):
                if(matrix[r][c]%2!=0):
                    cnt+=1
        return cnt
        
                

        
