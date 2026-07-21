class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n <= len(dp):
            return dp[n - 1]

        for i in range(3, n + 1):
            dp.append(dp[i - 2] + dp[i - 3])
        return dp[-1]