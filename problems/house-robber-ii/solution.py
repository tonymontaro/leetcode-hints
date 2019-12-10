class Solution:
    def rob(self, nums) -> int:
        """O(n) time and space"""
        if len(nums) <= 3:
            return max(nums) if nums else 0
        
        result = [0] * len(nums)
        result[:2] = nums[:2]
        max_num = max(nums[:2])
        for i in range(2, len(nums)-1):
            num = nums[i]
            result[i] = max(num + result[i-2], num + result[i-1]-nums[i-1])
            max_num = max(result[i], max_num)
        
        result = [0] * len(nums)
        result[1:2] = nums[1:3]
        for i in range(3, len(nums)):
            num = nums[i]
            result[i] = max(num + result[i-2], num + result[i-1]-nums[i-1])
            max_num = max(result[i], max_num)
        return max_num
        
