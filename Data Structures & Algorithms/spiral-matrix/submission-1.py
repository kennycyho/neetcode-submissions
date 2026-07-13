class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = t = 0
        r = len(matrix[0])
        b = len(matrix)
        res = []
        while l < r and t < b:
            for x in range(l, r):
                res.append(matrix[t][x])
            for y in range(t + 1, b):
                res.append(matrix[y][r - 1])
            if r - l == 1 or b - t == 1:
                return res
            for x in range(r - 2, l - 1, -1):
                res.append(matrix[b - 1][x])
            for y in range(b - 2, t, -1):
                res.append(matrix[y][l])
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res