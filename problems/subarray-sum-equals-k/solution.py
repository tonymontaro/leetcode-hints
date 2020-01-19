from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        """O(n) time and space"""
        result = 0
        sm = 0
        seen = defaultdict(int)
        seen[0] = 1
        for i, num in enumerate(nums):
            sm += num
            result += seen[sm - k]
            seen[sm] += 1
        return result

    
    ## No need for defaultdict
    class Solution:
    def subarraySum(self, nums, k: int) -> int:
        """O(n) time and space"""
        result = 0
        sm = 0
        seen = {0: 1}
        for num in nums:
            sm += num
            result += seen.get(sm - k, 0)
            seen[sm] = seen.get(sm, 0) + 1
        return result
