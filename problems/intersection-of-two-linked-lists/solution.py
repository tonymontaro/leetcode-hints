class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """O(n + m) time | O(1) space"""
        lnA = getLength(headA)
        lnB = getLength(headB)
        lower = headA if lnA < lnB else headB
        higher = headB if lnB > lnA else headA
        min_ = min(lnA, lnB)
        max_ = max(lnA, lnB)
        while min_ < max_:
            higher = higher.next
            max_ -= 1
        while lower:
            if lower == higher:
                return lower
            lower = lower.next
            higher = higher.next
        return None
        
def getLength(node):
    ln = 0
    while node:
        ln += 1
        node = node.next
    return ln
