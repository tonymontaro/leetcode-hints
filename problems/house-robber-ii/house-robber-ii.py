class Solution:
    def rob(self, nums) -> int:
        """O(n) time and space"""
        if len(nums) <= 2: return max(nums) if nums else 0
        return max(rob(nums[1:]), rob(nums[:-1]))

def rob(nums):
    result = [0] * len(nums)
    result[:2] = nums[:2]
    for i in range(2, len(nums)):
        num = nums[i]
        result[i] = max(num + result[i-2], num + result[i-1]-nums[i-1])
    return max(result[-2:])


## O(1) space => https://leetcode.com/problems/house-robber-ii/discuss/59978/6-lines-function-body
