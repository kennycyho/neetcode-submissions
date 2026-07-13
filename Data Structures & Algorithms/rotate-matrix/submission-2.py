class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        while l < r:
            for i in range(r - l - 1):
                topLeft = matrix[t][l+i]
                matrix[t][l+i] = matrix[b - 1 - i][l]
                matrix[b - 1 - i][l] = matrix[b-1][r - 1 - i]
                matrix[b-1][r - 1 - i] = matrix[t + i][r - 1]
                matrix[t + i][r - 1] = topLeft
            l += 1
            r -= 1
            t += 1
            b -= 1

