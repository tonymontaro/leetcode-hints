class Solution:
    def findDuplicate(self, nums):
        """O(n) time | O(1) space"""
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        head = nums[0]
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        return slow
