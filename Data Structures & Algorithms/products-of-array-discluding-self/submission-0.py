class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        p = 1
        for i in range(len(nums)):
            if i > 0:
                res[i] = p
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            if (i < len(nums) - 1):
                res[i] = res[i] * p
            p = p * nums[i]
        
        return res