class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, stack, total):
            nonlocal res
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(nums) or total > target:
                return
        
            stack.append(nums[i])
            dfs(i, stack, total + nums[i])
            stack.pop()

            dfs(i+1, stack, total)
        
        dfs(0, [], 0)
        return res