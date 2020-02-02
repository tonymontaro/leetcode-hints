class Solution:
    def canJump(self, nums) -> bool:
        """O(n) time | O(1) space"""
        if not nums: return True
        reach = nums[0]
        for i in range(1, len(nums)):
            if i > reach: return False
            reach = max(reach, (i + nums[i]))
        return True
