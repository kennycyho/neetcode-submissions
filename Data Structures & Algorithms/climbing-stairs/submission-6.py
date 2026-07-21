class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one = 2
        two = 1
        res = 0
        for i in range(3, n + 1):
            res = one + two
            two = one
            one = res
        
        return res