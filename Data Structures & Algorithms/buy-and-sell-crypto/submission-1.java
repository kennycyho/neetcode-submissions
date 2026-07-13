class Solution {
    public int maxProfit(int[] prices) {
        int diff = 0;
        int lo = prices[0];
        int hi = prices[0];
        for (int i = 1; i < prices.length; i++) {
            int price = prices[i];
            if (price < lo) {
                lo = price;
                hi = price;
            }
            else if (price > hi) {
                hi = price;
                if (hi - lo > diff) {
                    diff = hi - lo;
                }
            }
        }
        return diff;
    }
}
