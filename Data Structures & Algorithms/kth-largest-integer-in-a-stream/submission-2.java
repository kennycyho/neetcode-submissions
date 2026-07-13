class KthLargest {

    private int k;
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    public KthLargest(int k, int[] nums) {
        this.k=k;
        Arrays.sort(nums);
        for (int i = 0; i < k && i < nums.length; i++) {
            minHeap.add(nums[nums.length-1-i]);
        }
    }

    public int add(int val) {
        minHeap.add(val);
        if(minHeap.size() > k) {
            minHeap.remove();
        }
        return minHeap.peek();
    }
}
