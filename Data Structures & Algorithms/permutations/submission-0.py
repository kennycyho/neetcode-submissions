class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resultList = []

        def build(numsSubset, result):
            if len(numsSubset) == 0:
                resultList.append(result.copy())
            for i in range(len(numsSubset)):
                val = numsSubset.pop(i)
                result.append(val)
                build(numsSubset, result)
                result.pop()
                numsSubset.insert(i, val)

        build(nums, [])
        return resultList
