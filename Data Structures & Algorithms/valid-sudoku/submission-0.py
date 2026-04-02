class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                if val in cols[j]:
                    return False
                if val in rows[i]:
                    return False
                sq_index = int(i/3) * 3 + int(j/3)
                if val in squares[sq_index]:
                    return False
                cols[j].add(val)
                rows[i].add(val)
                squares[sq_index].add(val)
        return True