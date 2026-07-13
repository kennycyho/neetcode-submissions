class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char task : tasks) {
            count[task - 'A']++;
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int c : count) {
            if (c > 0) {
                maxHeap.offer(c);
            }
        }

        LinkedList<int[]> q = new LinkedList<>();
        int cycle = 0;
        while (!maxHeap.isEmpty() || !q.isEmpty()) {
            cycle++;
            if (!q.isEmpty() && q.peek()[1] == cycle) {
                maxHeap.offer(q.remove()[0]);
            }
            if (!maxHeap.isEmpty()) {
                int newCount = maxHeap.poll() - 1;
                if (newCount > 0) {
                    q.offer(new int[]{newCount, cycle + n + 1});
                }
            }
        }
        return cycle;
    }
}
