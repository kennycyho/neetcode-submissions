class Solution {

    public int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int numIslands(char[][] grid) {
        int count = 0;
        boolean[][] seen = new boolean[grid.length][grid[0].length];
        for (int y = 0; y < grid.length; y++){
            for (int x = 0; x < grid[y].length; x++) {
                if (seen[y][x]) {
                    continue;
                }
                if (grid[y][x] == '1') {
                    dfs(grid, x, y, seen);
                    count++;
                }
                seen[y][x] = true;
            }
        }
        return count;
    }

    public void dfs(char[][] grid, int x, int y, boolean[][] seen) {
        if (y >= 0 && y < grid.length && x >= 0 && x < grid[0].length) {
            char curr = grid[y][x];
            if (curr == '1' && !seen[y][x]) {
                seen[y][x] = true;
                for (int[] direction : directions) {
                    dfs(grid, x + direction[0], y + direction[1], seen);
                }
            }
            seen[y][x] = true;
        }
    }
}
