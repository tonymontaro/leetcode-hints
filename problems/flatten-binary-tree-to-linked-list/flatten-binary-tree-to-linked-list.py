class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        O(n) time | O(1) space -> in-place
        """
        def helper(node):
            if node:
                right = node.right
                if node.left:
                    node.right = node.left
                    last_left_node = helper(node.left)
                    node.left = None
                else:
                    last_left_node = node
                
                last_right_node = helper(right) or last_left_node
                if right:
                    last_left_node.right = right
                return last_right_node
        helper(root)
