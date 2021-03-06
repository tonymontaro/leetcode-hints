class Solution:
    def countBits(self, num: int):
        """O(n) time and space"""
        result = [0] * (num + 1)
        for i in range(1, num+1):
            result[i] = result[i//2]
            if i % 2 == 1: result[i] += 1
        return result

    
# Bit solution
class Solution:
    def countBits(self, num: int):
        """O(n) time and space"""
        result = [0] * (num + 1)
        for i in range(1, num+1):
            result[i] = result[i >> 1]
            if i % 2 == 1: result[i] += 1
        return result
