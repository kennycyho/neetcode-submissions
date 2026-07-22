class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        def solve(i) -> int:
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            if dp[i] > 0:
                return dp[i]
            
            if i + 1 < len(s) and s[i+1] == "0":
                if int(s[i] + s[i+1]) > 26:
                    return 0
                dp[i] = solve(i+2)
            elif i + 1 < len(s) and int(s[i] + s[i+1]) > 26:
                dp[i] = solve(i+1)
            else:
                dp[i] = solve(i+1) + solve(i+2) # single digit input is giving 1+1
            return dp[i]

        return solve(0)
        