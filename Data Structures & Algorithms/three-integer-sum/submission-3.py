class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k:
                        j += 1
                        k -= 1
                        if (nums[j] != nums[j-1] or nums[k] != nums[k+1]):
                            break
                elif sum > target:
                    k -= 1
                else:
                    j += 1
        return res