class Solution:
    def maxArea(self, nums) -> int:
        """O(n) time | O(1) space"""
        if not nums: return 0
        head = 0
        tail = len(nums)-1
        max_area = 0
        while head != tail:
            length = tail - head
            height = min(nums[head], nums[tail])
            max_area = max(max_area, length * height)
            
            if nums[tail] < nums[head]:
                tail -= 1
            else:
                head += 1
        return max_area
