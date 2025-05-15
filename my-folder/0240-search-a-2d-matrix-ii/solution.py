class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def binary(row, target):
        #         l, h = 0, len(row) - 1

        #         while l <= h:
        #             mid = (l + h)//2
        #             if row[mid] == target:
        #                 return True
        #             elif row[mid] < target:
        #                 l = mid + 1
        #             elif row[mid] > target:
        #                 h = mid - 1
        #         return False

        # for row_ind, row in enumerate(matrix):
        #     if row[0] <= target <= row[-1]:
        #         if binary(row, target):
        #             return True
        # return False
        row = len(matrix)
        col = len(matrix[0])
        i = row - 1
        j = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
