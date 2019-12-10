class Solution:
    def rob(self, nums):
        """O(n) time and space"""
        result = [0] * len(nums)
        result[:2] = nums[:2]
        for i in range(2, len(nums)):
            num = nums[i]
            result[i] = max(num + result[i-2], num + result[i-1]-nums[i-1])
        return max(result[-2:]) if result else 0
