class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix_len = len(matrix)
        row_len = len(matrix[0])
        i, j = 0, matrix_len - 1
        target_idx = None

        while i <= j:
            mid = (i + j) // 2

            if target < matrix[mid][0]:
                j = mid - 1
            elif matrix[mid][row_len-1] < target:
                i = mid + 1
            else:
                target_idx = mid
                break
        
        if target_idx is None:
            return False

        row = matrix[target_idx]
        print(row)

        i, j = 0, row_len - 1

        while i <= j:
            mid = (i + j) // 2

            if target < row[mid]:
                j = mid - 1
            elif row[mid] < target:
                i = mid + 1
            else:
                return True
        
        return False


