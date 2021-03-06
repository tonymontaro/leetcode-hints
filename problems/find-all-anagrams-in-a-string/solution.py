from collections import Counter

class Solution:
    def findAnagrams(self, word: str, substr: str):
        """O(n) time | O(1) space"""
        if not word or not substr: return []
        l = 0
        r = -1
        seen = 0
        ln = len(substr)
        counts = Counter(substr)
        counts = {char: -counts[char] for char in substr}
        result = []

        while r < len(word)-1:
            
            r += 1
            char = word[r]
            if char in counts:
                counts[char] += 1
                if counts[char] <= 0:
                    seen += 1
            if seen == ln:
                result.append(l)
            if r-l+1 == ln:
                char = word[l]
                l += 1
                if char in counts:
                    counts[char] -= 1
                    if counts[char] < 0:
                        seen -= 1
        return result
