class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        start = math.inf
        st = set(nums)
        for n in nums:
            curr = n
            count = 0
            while (curr  in st):
                if curr > start:
                    break
                count += 1
                curr += 1
            res = max(res, count)
        return res