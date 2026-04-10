class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startRow, startCol = 0, 0
        endRow, endCol = len(matrix), len(matrix[0])

        res = []
        while startCol < endCol and startRow < endRow:
            for c in range(startCol, endCol):
                res.append(matrix[startRow][c])
            startRow += 1
            
            for r in range(startRow, endRow):
                res.append(matrix[r][endCol - 1])
            endCol -= 1
            
            if not (startCol < endCol and startRow < endRow):
                break

            for c in range(endCol - 1, startCol - 1, -1):
                res.append(matrix[endRow - 1][c])
            endRow -= 1
            
            for r in range(endRow - 1, startRow - 1, -1):
                res.append(matrix[r][startCol])
            startCol += 1
        return res