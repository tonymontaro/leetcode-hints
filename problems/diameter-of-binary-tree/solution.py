class Solution:
    def diameterOfBinaryTree(self, node: TreeNode) -> int:
        """O(n) time | O(d) space"""
        self.max_len = 0
        def helper(node):
            if node is None: return 0
            left = helper(node.left)
            right = helper(node.right)
            self.max_len = max(self.max_len, (1 + left + right))
            return 1 + max(left, right)
        helper(node)
        return max(self.max_len-1, 0)
