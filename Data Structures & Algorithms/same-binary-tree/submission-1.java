/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public boolean isSameNode(TreeNode p, TreeNode q) {
        return p == null && q == null || (p != null && q != null && q.val == p.val);
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        LinkedList<TreeNode> q1 = new LinkedList<>();
        LinkedList<TreeNode> q2 = new LinkedList<>();

            if (!isSameNode(p, q)) {
                return false;
            }
            if (p == null && q == null) {
                return true;
            }
            else {
                q1.add(p);
                q2.add(q);
                while (!q1.isEmpty()) {
                    TreeNode node1 = q1.removeFirst();
                    TreeNode node2 = q2.removeFirst();
                    if (isSameNode(node1.left, node2.left)) {
                        if (node1.left != null) {
                            q1.add(node1.left);
                            q2.add(node2.left);
                        }
                    }
                    else {
                        return false;
                    }
                    if (isSameNode(node1.right, node2.right)) {
                        if (node1.right != null) {
                            q1.add(node1.right);
                            q2.add(node2.right);
                        }
                    }
                    else {
                        return false;
                    }
                }
                return true;
            }
    }
}
