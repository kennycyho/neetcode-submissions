class Solution:

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y) -> bool:
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return False
            val = grid[y][x]
            if val == "0" or val == "#":
                return False
            
            grid[y][x] = "#"
            for dir in self.directions:
                dfs(x + dir[0], y + dir[1])
            return True

        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if dfs(x, y):
                    count += 1
        return count