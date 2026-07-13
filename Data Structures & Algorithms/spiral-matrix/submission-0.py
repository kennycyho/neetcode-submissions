class Solution:
    def addOuterMatrix(self, matrix, l, r, t, b, ls) -> None:
        for x in range(l, r):
            ls.append(matrix[t][x])
        for y in range(t + 1, b):
            ls.append(matrix[y][r-1])
        if (t+1 == b or l+1 == r):
            return
        for x in reversed(range(l, r-1)):
            ls.append(matrix[b-1][x])
        for y in reversed(range(t+1, b-1)):
            ls.append(matrix[y][l])

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l = t = 0
        r = len(matrix[0])
        b = len(matrix)

        while(l < r and t < b):
            self.addOuterMatrix(matrix, l, r, t, b, res)
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res