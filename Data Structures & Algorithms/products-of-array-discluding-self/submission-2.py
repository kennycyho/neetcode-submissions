class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i, n in enumerate(nums):
            res[i] *= pre
            pre *= n
        
        post = 1
        for i, n in reversed(list(enumerate(nums))):
            res[i] *= post
            post *= n
        
        return res