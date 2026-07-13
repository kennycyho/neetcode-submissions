class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                res = max(res, profit)
            else:
                l = r
        return res