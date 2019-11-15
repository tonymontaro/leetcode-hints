class Solution:
    def pruneTree(self, root):
        """O(n) time | O(d) space | where d is depth of tree which can be logn"""
        prune_tree_helper(root)
        return root

def prune_tree_helper(node):
    total = node.val
    if node.left:
        total_left = prune_tree_helper(node.left)
        total += total_left
        if total_left == 0:
            node.left = None
    if node.right:
        total_right = prune_tree_helper(node.right)
        total += total_right
        if total_right == 0:
            node.right = None
    return total
