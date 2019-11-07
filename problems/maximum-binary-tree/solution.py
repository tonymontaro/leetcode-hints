class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f'{self.val} -> [{self.left}, {self.right}]'

def constructMaximumBinaryTree(nums):
    """O(N) time | O(1) space"""
    stack = []
    for num in nums:
        last = None
        num = TreeNode(num)
        while stack and num.val > stack[-1].val:
            last = stack.pop()
        if last:
            num.left = last
        if stack:
            stack[-1].right = num
        stack.append(num)
    return stack[0]
    
constructMaximumBinaryTree([3,2,1,6,0,5])
