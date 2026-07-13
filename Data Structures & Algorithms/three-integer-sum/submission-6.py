class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array
        #iterate array once until 3 nums are left
            #if curr == prev, skip
            #target = i * -1
            #lo = i+1
            #hi = len(nums) - 1

            #if sum == target return
            #if nums[lo] + nums[hi] < target
            #lo++
            #else hi++
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            n = nums[i]
            if i > 0 and n == nums[i-1]:
                continue
            target = n * -1
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum == target:
                    res.append([n, nums[lo], nums[hi]])
                elif curr_sum > target:
                    hi -= 1
                    continue
                lo += 1
                while lo < len(nums) and nums[lo] == nums[lo - 1]:
                    lo += 1
        return res