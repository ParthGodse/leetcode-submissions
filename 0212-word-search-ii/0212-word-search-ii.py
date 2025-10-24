class TrieNode():

    def __init__(self):
        self.children = {}
        self.endofword = False

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.insert(word)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, curr, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
            (r, c) in visit or board[r][c] not in curr.children):
                return

            visit.add((r, c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
            if curr.endofword:
                res.add(word)

            dfs(r + 1, c, curr, word)
            dfs(r - 1, c, curr, word)
            dfs(r, c + 1, curr, word)
            dfs(r, c - 1, curr, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)