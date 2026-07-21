class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [-1] * (len(nums) - 1)
        return max(self.robSub(0, nums[:-1], dp.copy()), self.robSub(0, nums[1:], dp.copy()))
    
    def robSub(self, i, nums, dp) -> int:
        if i >= len(nums):
            return 0
        if dp[i] > -1:
            return dp[i]
        
        dp[i] = max(self.robSub(i + 1, nums, dp), nums[i] + self.robSub(i + 2, nums, dp))
        return dp[i]
        