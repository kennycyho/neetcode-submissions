class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        ArrayDeque<int[]> stack = new ArrayDeque<>(); //[idx, temp]
        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            while (!stack.isEmpty() && temp > stack.peekLast()[1]) {
                int tailIdx = stack.removeLast()[0];
                res[tailIdx] = i - tailIdx;
            }
            stack.add(new int[]{i, temp});
        }
        return res;
    }
}
