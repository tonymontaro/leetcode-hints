from collections import Counter

def majorityElement(self, nums):
    "O(n) time | O(1) space"
    for key, val in Counter(nums).items():
        if val > len(nums)/2:
            return key

def majorityElement(self, nums):
    "O(n) time | O(1) space | source: http://www.cs.utexas.edu/~moore/best-ideas/mjrty/"
    majorElement = None
    count = 0
    for num in nums:
        if count == 0:
            majorElement = num
            count += 1
        elif num != majorElement:
            count -= 1
        else:
            count += 1
    return majorElement
