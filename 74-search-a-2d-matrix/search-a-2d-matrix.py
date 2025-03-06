class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        start, end = 0, rows * cols - 1

        while start <= end:
            mid = (start + end) // 2
            row, col = divmod(mid, cols)

            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False  
