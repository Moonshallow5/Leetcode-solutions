class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS,COLS=len(matrix),len(matrix[0])
        row,col=[False]*ROWS,[False]*COLS


        for r in range(ROWS):
            for c in range(COLS):
                if(matrix[r][c]==0):
                    row[r]=True
                    col[c]=True
        for r in range(ROWS):
            for c in range(COLS):
                if(row[r] or col[c]):
                    matrix[r][c]=0

        
        
