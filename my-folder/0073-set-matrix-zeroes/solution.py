class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rows, cols = len(matrix), len(matrix[0])
        # rows_to_replace = set()
        # cols_to_replace = set()

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             rows_to_replace.add(i)
        #             cols_to_replace.add(j)

        # for i in range(rows):
        #     for j in range(cols):
        #         if i in rows_to_replace or j in cols_to_replace:
        #             matrix[i][j] = 0
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
