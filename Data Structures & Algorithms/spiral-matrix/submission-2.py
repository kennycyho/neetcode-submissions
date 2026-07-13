class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = t = 0
        r = len(matrix[0])
        b = len(matrix)
        res = []
        while l < r and t < b:
            for x in range(l, r):
                res.append(matrix[t][x])
            t += 1
            for y in range(t, b):
                res.append(matrix[y][r - 1])
            r -= 1
            if not (l < r and t < b):
                return res
            for x in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][x])
            b -= 1
            for y in range(b - 1, t - 1, -1):
                res.append(matrix[y][l])
            l += 1
        return res