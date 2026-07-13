class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums);
        return nums;
    }

    private static void mergeSort(int[] nums) {
        if (nums.length <= 1) {
            return;
        }

        int mid = nums.length / 2;
        int[] leftArray = new int[mid];
        int[] rightArray = new int[nums.length - mid];

        for (int i = 0; i < mid; i++) {
            leftArray[i] = nums[i];
        }
        for (int j = 0; j < rightArray.length; j++) {
            rightArray[j] = nums[mid + j];
        }

        mergeSort(leftArray);
        mergeSort(rightArray);
        merge(leftArray, rightArray, nums);
    }

    private static void merge(int[] leftArray, int[] rightArray, int[] nums) {
        int i = 0;
        int j = 0;
        int n = 0;

        while (i < leftArray.length && j < rightArray.length) {
            if (leftArray[i] <= rightArray[j]) {
                nums[n] = leftArray[i];
                i++;
            }
            else {
                nums[n] = rightArray[j];
                j++;
            }
            n++;
        }
        while (i < leftArray.length) {
            nums[n] = leftArray[i];
            i++;
            n++;
        }
        while (j < rightArray.length) {
            nums[n] = rightArray[j];
            j++;
            n++;
        }
    }
}