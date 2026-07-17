class Solution:
    directions = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(x: int, y: int, charIdx: int) -> bool:
            if charIdx == len(word):
                return True
            if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0:
                return False
            if board[y][x] == '#':
                return False
            if board[y][x] != word[charIdx]:
                return False

            char = board[y][x]
            board[y][x] = '#'
            for dir in self.directions:
                if dfs(x + dir[0], y + dir[1], charIdx + 1):
                    return True
            board[y][x] = char
            return False

        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(x, y, 0):
                    return True
        return False