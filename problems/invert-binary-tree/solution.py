class Solution:
    def invertTree(self, node: TreeNode) -> TreeNode:
        """O(n) time | O(d) space | d->depth"""
        if node:
            node.left, node.right = node.right, node.left
            self.invertTree(node.right)
            self.invertTree(node.left)
        return node
