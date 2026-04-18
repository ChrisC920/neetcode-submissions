class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()

        for word in words:
            curr = root

            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isEnd = True
        res = set()
        visited = set()

        def dfs(r, c, node, word):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, node, word)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)