class Solution {
    public int maxProfit(int[] prices) {
        int diff = 0;
        int lowest = prices[0];
        for (int i = 1; i < prices.length; i++) {
            int price = prices[i];
            if (price < lowest) {
                lowest = price;
            }
            if (price - lowest > diff) {
                diff = price - lowest;
            }
        }
        return diff;
    }
}
