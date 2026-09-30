class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = []

        def backtrack(r):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in board])
                return
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board.append(c)
                backtrack(r + 1)
                board.pop()
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res