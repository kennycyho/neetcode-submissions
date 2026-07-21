class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def choose(i) -> int:
            if i >= len(nums):
                return 0
            if dp[i] > -1:
                return dp[i]
            
            dp[i] = nums[i] + choose(i + 2)
            return max(dp[i], choose(i + 1))
    
        return choose(0)