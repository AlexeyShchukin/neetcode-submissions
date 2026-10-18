class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mdl_row_idx = (left + right) // 2
            if target in matrix[mdl_row_idx]:
                l = 0
                r = len(matrix[mdl_row_idx]) - 1
                while l <= r:
                    middle_idx = (l + r) // 2
                    if target == matrix[mdl_row_idx][middle_idx]:
                        return True
                    elif target < matrix[mdl_row_idx][middle_idx]:
                        r = middle_idx - 1
                    else:
                        l = middle_idx + 1
            elif target > matrix[mdl_row_idx][-1]:
                left = mdl_row_idx + 1
            else:
                right = mdl_row_idx - 1
        return False
