import numpy as np

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        l = t = 0
        r = b = n
        currNum = 1
        while l < r and t < b:
            for x in range(l, r):
                matrix[t][x] = currNum
                currNum += 1
            t += 1
            for y in range(t, b):
                matrix[y][r - 1] = currNum
                currNum += 1
            r -= 1
            if not (l < r and t < b):
                return matrix
            for x in range(r - 1, l - 1, -1):
                matrix[b - 1][x] = currNum
                currNum += 1
            b -= 1
            for y in range(b - 1, t - 1, -1):
                matrix[y][l]  = currNum
                currNum += 1
            l += 1
        return matrix