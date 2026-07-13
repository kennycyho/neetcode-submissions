class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        st = set(nums)
        for n in nums:
            if (n - 1 in st):
                continue
            curr = n
            count = 0
            while (curr  in st):
                count += 1
                curr += 1
            res = max(res, count)
        return res