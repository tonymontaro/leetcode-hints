class Solution:
    def sortColors(self, nums) -> None:
        """O(n) time | O(1) space"""
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        l = i = 0
        r = len(nums)-1
        while i <= r:
            num = nums[i]
            if num == 2:
                swap(i, r)
                r -= 1
            elif num == 0 and i > l:
                swap(i, l)
                l += 1
            else:
                i += 1
