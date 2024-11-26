class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid = [list(column) for column in zip(*grid)]
        print(transposed_grid)
        print(grid)
        cnt=0

        for i in transposed_grid:
            for j in grid:
                if(i==j):
                    cnt+=1

        return cnt

        
