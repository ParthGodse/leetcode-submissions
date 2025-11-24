class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        def max_row_in_col(mat, n, m, colnumber):

            best_row = 1
            best_val = mat[1][colnumber]

            for row in range(n):  # interior rows
                if mat[row][colnumber] > best_val:
                    best_val = mat[row][colnumber]
                    best_row = row

            return best_row

        def core(mat, n, m):
            low = 0
            high = m - 1

            while low <= high:
                mid = (low + high) // 2
                row = max_row_in_col(mat, n, m, mid)

                left = mat[row][mid - 1] if mid - 1 >= 0 else -1
                right = mat[row][mid + 1] if mid + 1 < m else -1
                
                if mat[row][mid] > left and mat[row][mid] > right:
                    return [row, mid]
                elif mat[row][mid] < left:
                    high = mid - 1
                else:
                    low = mid + 1

            return [-1, -1]

        return core(mat, n, m)