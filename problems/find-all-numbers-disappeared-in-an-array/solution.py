def findDisappearedNumbers(self, nums):
    """O(n) time | O(n) space"""
    return set(range(1, len(nums)+1)) - set(nums)

def findDisappearedNumbers(self, nums):
    """O(n) time | O(1) space"""
    for idx in range(len(nums)):
        if nums[idx] > 0:
            while nums[idx] > 0:
                num = nums[idx]
                if nums[num-1] < 0:
                    nums[idx] = 0
                else:
                    nums[idx], nums[num-1] = nums[num-1], -nums[idx]
    return [num for num in range(1, len(nums)+1) if nums[num-1] == 0]

def findDisappearedNumbers(self, nums):
    """O(n) time | O(1) space"""
    for i in range(len(nums)):
        idx = abs(nums[i])-1
        nums[idx] = -abs(nums[idx])
    return [num for num in range(1, len(nums)+1) if nums[num-1] > 0]
