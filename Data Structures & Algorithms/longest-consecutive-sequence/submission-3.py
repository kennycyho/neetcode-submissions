class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        st = set(nums)
        for n in nums:
            curr = n
            count = 1
            while (curr + 1 in st):
                count += 1
                curr += 1
            res = max(res, count)
        return res