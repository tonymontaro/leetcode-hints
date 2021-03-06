class Solution:
    def partitionLabels(self, string):
        """O(N) time | O(1) space"""
        chars = {}
        for i, char in enumerate(string):
            if char in chars:
                chars[char][1] = i
            else:
                chars[char] = [i, i]

        partitions = []
        i = prev = 0
        while i < len(string):
            char = string[i]
            i = chars[char][1]
            while char:
                for c, pos in chars.items():
                    if pos[0] <= i and pos[1] > i:
                        i = pos[1]
                else:
                    char = None
            partitions.append(i - prev + 1)
            i += 1
            prev = i
        return partitions

    
# Even better, idea from:
# https://leetcode.com/problems/partition-labels/discuss/298474/Python-two-pointer-solution-with-explanation
class Solution:
    def partitionLabels(self, string):
        """O(N) time | O(1) space"""
        chars = {c:i for i,c in enumerate(string)}
        left = right = 0
        partitions = []

        for i, char in enumerate(string):
            right = max(right, chars[char])

            if i == right:
                partitions.append(right - left + 1)
                left = right + 1
        return partitions
