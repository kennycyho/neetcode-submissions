class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robSub(i, end: int, dp) -> int:
            if i > end:
                return 0
            if dp[i] > -1:
                return dp[i]
            
            dp[i] = max(robSub(i + 1, end, dp), nums[i] + robSub(i + 2, end, dp))
            return dp[i]


        dp = [-1] * len(nums)
        return max(robSub(0, len(nums) - 2, dp.copy()), robSub(1, len(nums) - 1, dp.copy()))
    

        