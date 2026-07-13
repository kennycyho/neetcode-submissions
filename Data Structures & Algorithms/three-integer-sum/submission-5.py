class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            target = -n
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum == target:
                    res.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif sum > target:
                    k -= 1
                else:
                    j += 1
        return res