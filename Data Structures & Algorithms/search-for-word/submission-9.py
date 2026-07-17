

class Solution:
    directions = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(x, y, charIdx: int, seen: list[list[bool]]) -> bool:
            if charIdx == len(word):
                return True
            if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0:
                return False
            if seen[y][x]:
                return False
            if board[y][x] != word[charIdx]:
                return False

            seen[y][x] = True
            for dir in self.directions:
                if dfs(x + dir[0], y + dir[1], charIdx + 1, seen):
                    return True
            seen[y][x] = False
            return False
    
        seen = [[False] * len(board[0]) for i in range(len(board))]
        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(x, y, 0, seen):
                    return True
        return False
    
