class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        L = 0
        R = rows * columns - 1
        n = columns

        while L <= R:
            mid = (L + R) // 2

            if target > matrix[mid // n][mid % n]:
                L = mid + 1
            elif target < matrix[mid // n][mid % n]:
                R = mid - 1
            else:
                return True
        return False