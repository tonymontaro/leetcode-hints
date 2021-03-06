from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, sm: int) -> int:
        """O(n) time and space"""
        def helper(node, total, sm, seen, rs):
            if node:
                total += node.val
                if seen[total - sm] > 0:
                    rs['val'] += seen[total - sm]
                seen[total] += 1
                helper(node.left, total, sm, seen, rs)
                helper(node.right, total, sm, seen, rs)
                seen[total] -= 1
        rs = {'val': 0}
        seen = defaultdict(int)
        seen[0] = 1
        helper(root, 0, sm, seen, rs)
        return rs['val']
