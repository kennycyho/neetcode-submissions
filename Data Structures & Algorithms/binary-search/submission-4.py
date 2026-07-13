class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            m = (lo + hi) // 2
            v = nums[m]
            if v == target:
                return m
            elif v < target:
                lo = m + 1
            else:
                hi = m
        return -1
