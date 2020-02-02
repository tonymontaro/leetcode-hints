class Solution:
    def canJump(self, nums) -> bool:
        """O(n) time | O(1) space"""
        if not nums: return True
        reach = nums[0]
        for i in range(1, len(nums)):
            if i > reach: return False
            reach = max(reach, (i + nums[i]))
        return True

# iterative solution
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        """O(max(l1, l2) time | O(1) space)"""
        head = None
        prev = None
        carry = 0
        while l1 or l2:
            left = right = 0
            if l1:
                left = l1.val
                l1 = l1.next
            if l2:
                right = l2.val
                l2 = l2.next
            carry, mod = divmod((left + right + carry), 10)
            node = ListNode(mod)
            if prev is None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node
        if carry > 0:
            node.next = ListNode(carry)
        return head
    
    
    # very good solution
    class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = l1.val + l2.val
        carrier, out = divmod(l1.val+l2.val, 10)
        result = ListNode(out)
        temp = result
        
        l1=l1.next
        l2=l2.next
        while l1 or l2 or carrier:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carrier, out = divmod(val1+val2+carrier, 10)
            
            temp.next = ListNode(out)
            temp = temp.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result
