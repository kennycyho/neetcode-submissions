class Solution {
    public int search(int[] nums, int t) {
        int result = -1;
        int l = 0;
        int r = nums.length;
        int lastNum = nums[nums.length - 1];
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (t == nums[mid]) {
                result = mid;
                break;
            }
            if (t > lastNum && nums[mid] <= lastNum) {
                r = mid;
            }
            else if (t <= lastNum && nums[mid] > lastNum) {
                l = mid + 1;
            }
            else {
                if (t < nums[mid]) {
                    r = mid;
                }
                else {
                    l = mid + 1;
                }
            }
        }
        return result;
    }
}
