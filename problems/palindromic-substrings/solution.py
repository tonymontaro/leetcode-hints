class Solution:
    def countSubstrings(self, word: str) -> int:
        """O(n^2) time | O(1) space"""
        def count_pal(l, r, word):
            rs = 0
            while l >= 0 and r < len(word) and word[l] == word[r]:
                rs += 1
                l -= 1
                r += 1
            return rs
        result = 0
        for i in range(len(word)):
            result += count_pal(i, i, word)
            result += count_pal(i-1, i, word)
        return result

## Time can be improved to O(n) with Manacher's Algorithm
