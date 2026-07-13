class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, n in enumerate(nums):
            t = -n
            l, r = i + 1, len(nums) - 1
            while (l < r):
                sum = nums[l] + nums[r]
                if sum == t:
                    res.add((n, nums[l], nums[r]))
                    l, r = l + 1, r - 1
                elif sum > t:
                    r-=1
                else:
                    l+=1
            
        
        return list(res)