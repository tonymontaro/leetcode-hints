from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for item in strs:
            key_str = tuple(sorted(item))
            result[key_str].append(item)
        return result.values()
