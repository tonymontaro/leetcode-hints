class Solution:
    def subsets(self, nums):
        """O(n^2) | not sure"""
        self.result = [[]]
        def helper(start, nums, prev_set):
            for i in range(start, len(nums)):
                if nums[i] not in prev_set:
                    new_set = set(prev_set)
                    new_set.add(nums[i])
                    self.result.append(new_set)
                    helper(i+1, nums, new_set)
        helper(0, nums, set())
        return self.result
