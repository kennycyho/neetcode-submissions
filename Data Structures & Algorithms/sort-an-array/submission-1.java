class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    private static void mergeSort(int[] nums, int l, int r) {
        if (l >= r) {
            return;
        }
        int mid = (l + r) / 2;
        mergeSort(nums, l, mid);
        mergeSort(nums, mid + 1, r);
        merge(nums, l, mid, r);
    }

    private static void merge(int[] nums, int l, int mid, int r) {
        List<Integer> temp = new ArrayList<Integer>();
        int i = l;
        int j = mid + 1;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                temp.add(nums[i]);
                i++;
            }
            else {
                temp.add(nums[j]);
                j++;
            }
        }
        while (i <= mid) {
            temp.add(nums[i]);
            i++;
        }
        while (j <= r) {
            temp.add(nums[j]);
            j++;
        }

        for (int t = 0; t < temp.size(); t++) {
            nums[l + t] = temp.get(t);
        }
    }
}