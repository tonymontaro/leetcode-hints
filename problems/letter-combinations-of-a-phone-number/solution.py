class Solution:
    def letterCombinations(self, digits: str):
        """O(4^n) time | O(n) space excluding the result"""
        if not digits: return []
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []
        self.solve(0, '', digits)
        return self.result
        
    def solve(self, i, prev, digits):
        if i == len(digits):
            self.result.append(prev)
        else:
            for char in self.mapping[digits[i]]:
                self.solve(i+1, prev+char, digits)
