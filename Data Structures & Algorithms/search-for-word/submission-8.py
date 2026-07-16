class Solution:
    directions = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, charIdx: int, stack: List[str], seen: List[List[bool]]) -> bool:
            if "".join(stack) == word:
                return True
            if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0:
                return False
            if seen[y][x]:
                return False
            if charIdx >= len(word) or board[y][x] != word[charIdx]:
                return False

            seen[y][x] = True
            stack.append(board[y][x])
            for dir in self.directions:
                if dfs(x + dir[0], y + dir[1], charIdx + 1, stack, seen):
                    return True
            stack.pop()
            seen[y][x] = False
            return False
    
        seen = [[False] * len(board[0]) for i in range(len(board))]
        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(x, y, 0, [], seen):
                    return True
        return False