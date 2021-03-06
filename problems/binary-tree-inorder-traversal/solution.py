from collections import deque

class Solution:
    def inorderTraversal(self, root: TreeNode):
        """O(n) time and space | iterative in-order traversal"""
        if not root: return []
        items = deque([root])
        result = []
        while items:
            if items[0].left:
                items.appendleft(items[0].left)
                items[1].left = None
            else:
                temp = items.popleft()
                result.append(temp.val)
                if temp.right:
                    items.appendleft(temp.right)
        return result
