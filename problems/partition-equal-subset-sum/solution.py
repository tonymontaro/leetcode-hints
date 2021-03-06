class Solution:
    def canPartition(self, nums) -> bool:
        """O(sum(nums) * n) time | O(n) space"""
        if not nums: return True
        nums = sorted(nums)
        half = sum(nums)/2
        if not half.is_integer(): return False
        return sub_set_sum(nums, int(half))

def sub_set_sum(arr, target):
    prev = [False] * (target + 1)
    prev[0] = True
    for num in arr:
        current = [False] * (target + 1)
        for i in range(target+1):
            if i < num:
                current[i] = prev[i]
            else:
                current[i] = prev[i-num] or prev[i]
        if current[-1]:
            return True
        prev = current
    return prev[-1]
