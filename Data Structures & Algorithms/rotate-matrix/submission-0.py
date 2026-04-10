class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        print(matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix[0]) // 2):
                matrix[r][c], matrix[r][len(matrix[0]) - c - 1] = matrix[r][len(matrix[0]) - c - 1], matrix[r][c]
                