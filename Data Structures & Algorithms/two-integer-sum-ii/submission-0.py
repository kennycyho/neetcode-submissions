class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)
        while (l < r):
            curSum = numbers[l - 1] + numbers[r - 1]
            if (curSum == target):
                return [l, r]
            elif curSum < target:
                l += 1;
            else:
                r -= 1;
        return [];