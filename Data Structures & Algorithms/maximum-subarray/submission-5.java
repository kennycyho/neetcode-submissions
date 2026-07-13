class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int total = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            if (total < 0) {
                total = n;
            }
            else {
                total += n;
            }
            maxSum = Math.max(maxSum, total);
        }
        return maxSum;
    }
}
