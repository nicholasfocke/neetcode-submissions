class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = top + ((bottom - top) // 2)
            row = matrix[mid]

            if target > row[-1]:
                top = mid + 1
            
            elif target < row[0]:
                bottom = mid - 1
            else:
                break
        l = 0
        r = len(row) - 1

        if top > bottom:
            return False

        while l <= r:
            mid_row = l + ((r - l) //2)

            if row[mid_row] == target:
                return True
            elif target < row[mid_row]:
                r = mid_row - 1
            else:
                l = mid_row + 1
        return False