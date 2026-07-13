class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        int last = nums[nums.length - 1];
        int[] subArr = Arrays.copyOfRange(nums, 0, nums.length - 1);
        if (nums.length == 1) {
            if (target % last == 0 || target == last) {
                result.add(createListOfNums(last, target / last));
            }
            return result;
        }
        for (int i = 1; i <= target / last; i++) {
            int curTarget = target - last * i;
            List<Integer> suffix = createListOfNums(last, i);
            if (curTarget == 0) {
                result.add(suffix);
            }
            else {
                for (List<Integer> l : combinationSum(subArr, curTarget)) {
                        l.addAll(suffix);
                        result.add(l);
                    }
            }
        }
        result.addAll(combinationSum(subArr, target));
        return result;
    }
    private List<Integer> createListOfNums(int num, int length) {
        List<Integer> l = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            l.add(num);
        }
        return l;
    }
}
