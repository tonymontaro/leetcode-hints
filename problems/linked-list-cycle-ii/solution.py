class Solution:
    def detectCycle(self, head):
        """O(n) time | O(1) space"""
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return find_cycle(head, slow)
        return None

def find_cycle(head, slow):
    while head is not slow:
        head = head.next
        slow = slow.next
    return slow
