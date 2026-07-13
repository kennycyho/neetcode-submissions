class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length;
        int pivot =  nums[nums.length - 1];
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target) return mid;
            else if (target <= pivot && nums[mid] > pivot) l = mid + 1;
            else if (target > pivot && nums[mid] <= pivot) r = mid ;
            else {
                if (nums[mid] < target) l = mid + 1;
                else r = mid;
            }
        }
        return -1;
    }
}
