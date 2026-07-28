class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [999999] * (amount + 1)
        def dfs(t: int) -> int:
            if t == 0:
                return 0
            if dp[t] != 999999:
                return dp[t]

            res = 99999
            for n in coins:
                if (t-n) >= 0:
                    dp[t-n] = dfs(t-n)
                    res = min(1 + dp[t-n], res)
            return res

        res =  dfs(amount)
        if res == 99999:
            return -1
        return res