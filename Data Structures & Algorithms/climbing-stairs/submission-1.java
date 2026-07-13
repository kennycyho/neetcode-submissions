class Solution {
    public int recurse(int n, int[] mem) {
        
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        if (mem[n] == 0) {
            mem[n] = recurse(n-1, mem) + recurse(n-2, mem);
        }
        return mem[n];
    }

    public int climbStairs(int n) {
        return recurse(n, new int[n+1]);
    }

}
