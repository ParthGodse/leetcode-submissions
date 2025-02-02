class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for row in matrix:
        #     for val in row:
        #         if val == target:
        #             return True
        # return False
            def binary(row, target):
                l, h = 0, len(row) - 1

                while l <= h:
                    mid = (l + h)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    elif row[mid] > target:
                        h = mid - 1
                return False

            for row_ind, row in enumerate(matrix):
                if row[0] <= target <= row[-1]:
                    if binary(row, target):
                        return True
            return False
