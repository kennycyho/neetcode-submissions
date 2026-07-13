class Solution:
    directions = [[0,1], [1,0], [-1,0], [0,-1]]
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(idx: int, x: int, y: int):
            if idx >= len(word):
                return False
            if not (0 <= x < len(board[0]) and 0 <= y < len(board)):
                return False
            if board[y][x] != word[idx]:
                return False
            if board[y][x] == "#":
                return False
            if idx == len(word) - 1:
                return True

            currChar = board[y][x]
            board[y][x] = "#"
            for d in self.directions:
                if dfs(idx + 1, x + d[0], y + d[1]):
                    return True
            board[y][x] = currChar
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if dfs(0, x, y):
                    return True
        return False