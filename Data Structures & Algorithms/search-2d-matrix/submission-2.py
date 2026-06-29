class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t < b - 1:
            mid = (b + t) // 2
            if matrix[mid][0] <= target:
                t = mid
            else:
                b = mid - 1
        l, r = 0, len(matrix[0]) - 1
        print(t)
        while l < r:
            mid = (l + r) // 2
            if target == matrix[t][mid]:
                return True
            if target < matrix[t][mid]:
                r = mid
            else:
                l = mid + 1
        return False