class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot = 0
        top = len(matrix) - 1
        while bot <= top:
            c = (bot + top) // 2
            if matrix[c][0] == target:
                return True
            elif matrix[c][0] < target:
                l = 0
                r = len(matrix[c]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[c][m] == target:
                        return True
                    elif matrix[c][m] < target:
                        l = m + 1
                    elif matrix[c][m] > target:
                        r = m - 1
                bot = c + 1
            elif matrix[c][0] > target:
                l = 0
                r = len(matrix[c]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[c][m] == target:
                        return True
                    elif matrix[c][m] < target:
                        l = m + 1
                    elif matrix[c][m] > target:
                        r = m - 1
                top = c - 1
        return False