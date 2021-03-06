import bisect

class Solution:
    def lengthOfLIS(self, nums) -> int:
        """O(nlogn) time | O(n) space"""
        lens = []
        for num in nums:
            idx = bisect.bisect_left(lens, num)
            if len(lens) == idx:
                lens.append(num)
            elif lens[idx] > num:
                lens[idx] = num
        return len(lens)
