class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            int[] row = matrix[i];
            if (row[0] == target || row[row.length - 1] == target) {
                return true;
            }
            else if (row[0] < target && target < row[row.length - 1]) {
                //binary search row
                int l = 0, r = row.length;
                while (l < r) {
                    int m = (l + r) / 2;
                    if (row[m] == target) {
                        return true;
                    }
                    else if (row[m] < target) {
                        l = m + 1;
                    }
                    else {
                        r = m;
                    }
                }
                return false;
            }
        }
        return false;
    }
}
