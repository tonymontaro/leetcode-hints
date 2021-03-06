class Solution:
    def permute(self, nums):
        """O(n! * n)"""
        def helper(nums, added, result):
            if len(added) == len(nums):
                result.append(added.keys())
                return
            for num in nums:
                if num not in added:
                    new_added = dict(added)
                    new_added[num] = None
                    helper(nums, new_added, result)
        result = []
        helper(nums, {}, result)
        return result
