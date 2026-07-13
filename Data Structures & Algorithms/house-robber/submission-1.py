class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)
        def dfs(i) -> int:
            if i >= len(nums):
                return 0
            if mem[i] < 0:
                mem[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return mem[i]
        return dfs(0)