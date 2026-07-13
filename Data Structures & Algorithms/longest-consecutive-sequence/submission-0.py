class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for n in nums:
            count = 1
            nextNum = n + 1
            while nextNum in numSet:
                count += 1
                nextNum += 1
            longest = max(count, longest)
        return longest