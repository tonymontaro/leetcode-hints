class Solution(object):
    def insertIntoBST(self, root, val):
        node = root
        while True:
            if val > node.val:
                if node.right is None:
                    node.right  = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left  = TreeNode(val)
                    return root
                else:
                    node = node.left
