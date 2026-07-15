class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, stack: List[int], currSum: int) -> None:
            if i >= len(nums):
                return 
            if currSum > target:
                return
            if currSum == target:
                res.append(stack.copy())
                return
            
            stack.append(nums[i])
            dfs(i, stack, nums[i] + currSum)
            stack.pop()

            dfs(i + 1, stack, currSum)

        dfs(0, [], 0)
        return res