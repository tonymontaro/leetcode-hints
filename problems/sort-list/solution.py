class Solution:
    def sortList(self, node: ListNode) -> ListNode:
        """O(nlogn) time"""
        if not node or node.next is None: return node
        
        slow = node
        fast = node.next
        
        while fast is not None:
            if fast.next is None: break
            slow = slow.next
            fast = fast.next.next
        
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(node)
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1, l2):
        def merge(root, l1, l2):
            if not l1 and not l2:
                return
            if (not l1 and l2) or (l1 and l2 and l1.val > l2.val):
                l1, l2 = l2, l1
            if root:
                root.next = l1
            merge(l1, l2, l1.next)
            return l1
        
        return merge(None, l1, l2)
        
        
        
# Clean solution but not mine (https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code), checking runtime
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))
