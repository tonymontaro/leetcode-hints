class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) < 1: return
        return self.helper(preorder, inorder)
    
    def helper(self, preorder, inorder):
        if len(preorder) < 1: return None
        node = TreeNode(preorder[0])
        if len(preorder) == 1: return node
        idx = inorder.index(preorder[0])
        node.left = self.helper(preorder[1:idx+1], inorder[0:idx])
        node.right = self.helper(preorder[idx+1:], inorder[idx+1:])
        return node
