class Solution {

    private void dfs(int[] nums, int target, List<List<Integer>> resultList, int i, List<Integer> currentList, int total) {
        if (total == target) {
            resultList.add(new ArrayList<>(currentList));
            return;
        }
        if (i >= nums.length || total > target) {
            return;
        }
        dfs(nums, target, resultList, i + 1, currentList, total);
        currentList.add(nums[i]);
        dfs(nums, target, resultList, i, currentList, total + nums[i]);
        currentList.removeLast();
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> resultList = new ArrayList<>();
        dfs(nums, target, resultList, 0, new ArrayList<Integer>(), 0);
        return resultList;
    }
}