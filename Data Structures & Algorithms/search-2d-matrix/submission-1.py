class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        # for r in range(len(matrix)):
        #     for c in range(len(matrix) + 1):
        #         print(matrix[r][c])
        
        for r in range(len(matrix)):
            left = 0
            right = len(matrix[r]) - 1
            if target <= matrix[r][right]:
                while left <= right:
                    middle = (left + right) // 2
                    if target > matrix[r][middle]:
                        left = middle + 1
                    elif target < matrix[r][middle]:
                        right = middle - 1
                    else:
                        return True
                    
        return False
                    
        
        