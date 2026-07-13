import copy

class Solution:
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #dfs cells along pacific, get set
        pacificVisited = set()
        pacificMtx = copy.deepcopy(heights)
        for y in range(len(heights)):
            self.dfs(y, 0, -1, pacificMtx, pacificVisited)
        for x in range(len(heights[0])):
            self.dfs(0, x, -1, pacificMtx, pacificVisited)

        #dfs cells along atlantic, get set
        atlanticVisited = set()
        atlanticMtx = copy.deepcopy(heights)
        for y in range(len(heights)):
            self.dfs(y, len(heights[0]) - 1, -1, atlanticMtx, atlanticVisited)
        for x in range(len(heights[0])):
            self.dfs(len(heights) - 1, x, -1, atlanticMtx, atlanticVisited)

        #result is intersect of two sets
        print(pacificVisited)
        print(atlanticVisited)
        print(heights)
        common = pacificVisited.intersection(atlanticVisited)
        res = []
        for tup in common:
            res.append(list(tup))
        return res

    def dfs(self, y, x, prev, mtx, visited: Set) -> None:
        if x < 0 or y < 0 or x >= len(mtx[0]) or y >= len(mtx):
            return
        val = mtx[y][x]
        if val < 0:
            return
        if val < prev:
            return

        #add cell to visited set
        #set cell to -1
        visited.add((y, x))
        mtx[y][x] = -1
    
        #dfs all neighouring valid cells (if not -1)
        for move in self.directions:
            self.dfs(y + move[0], x + move[1], val, mtx, visited)