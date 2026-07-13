class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        low = high = prices[0]
        for p in prices:
            if p < low:
                low = high = p
            if p > high:
                high = p
                maxProfit = max(maxProfit, high - low)
        return maxProfit