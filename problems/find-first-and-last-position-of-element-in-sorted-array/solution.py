import bisect

class Solution:
    def searchRange(self, nums, target: int):
        """O(logn) time | O(1) space"""
        res = [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]
        return res if nums and nums[res[1]] == target else [-1, -1]
