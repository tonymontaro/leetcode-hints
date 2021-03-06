class Solution:
    def rob(self, root) -> int:
        """O(n) time | O(d) space | d -> depth of tree"""
        def helper(node):
            if node is None:
                return [0, 0]
            left = helper(node.left)
            right = helper(node.right)
            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0
            
            res_second = max(left) + max(right)
            left_max = max(left[0] - left_val, left[1])
            right_max = max(right[0] - right_val, right[1])
            return [node.val + left_max + right_max, res_second]
        return max(helper(root))
