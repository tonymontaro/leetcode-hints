class Solution:
    """O(N) time | O(1) space"""
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.solveNode(root, prev=0)
        return root
    
    def solveNode(self, node, prev=0):
        if node is None:
            return 0
        right = self.solveNode(node.right, prev) + node.val
        node.val = (right + prev)
        left = self.solveNode(node.left, node.val)
        return (left + right)
