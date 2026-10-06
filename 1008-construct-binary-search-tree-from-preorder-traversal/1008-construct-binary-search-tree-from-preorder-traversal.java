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
    int idx = 0;

    public TreeNode bstFromPreorder(int[] preorder) {
        return build(preorder, Integer.MAX_VALUE);
    }

    private TreeNode build(int[] pre, int bound) {
        if (idx == pre.length || pre[idx] > bound) return null;

        TreeNode node = new TreeNode(pre[idx++]);
        node.left = build(pre, node.val);   // left values must be < node.val
        node.right = build(pre, bound);     // right values must be < parent's bound
        return node;
    }
}