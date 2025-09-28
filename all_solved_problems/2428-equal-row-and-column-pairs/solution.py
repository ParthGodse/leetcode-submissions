class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = Counter()
        for row in grid:
            row_tuple = tuple(row)  
            row_count[row_tuple] += 1  

        col_count = Counter()
        for col in range(n):
            column_tuple = []
            for row in range(n):
                column_tuple.append(grid[row][col])  
            col_tuple = tuple(column_tuple)  
            col_count[col_tuple] += 1  
            
        result = 0
        for row_tuple in row_count:
            if row_tuple in col_count:
                result += row_count[row_tuple] * col_count[row_tuple]

        return result
