class Solution:
    def numSquares(self, n: int) -> int:
        """O(n * sqrt(n))"""
        max_num = int(n**(1/2))
        current = list(range(n+1))
        
        for num in range(1, max_num+1):
            sq = num**2
            
            for i in range(n+1):
                if i >= sq:
                    current[i] = min(current[i], current[i-sq]+1)
        return current[-1]

# same idea but much faster because the result is cached between test cases
class Solution:
    current = [] # cache result between test cases
    def numSquares(self, n: int) -> int:
        """O(n * sqrt(n))"""
        current = self.current
        if n < len(current):
            return current[n]
        max_sq_num = int(n**(1/2))
        min_num = len(self.current)
        current += list(range(min_num, n+1))
        
        for num in range(1, max_sq_num+1):
            sq = num**2
            
            for i in range(min_num, n+1):
                if i >= sq:
                    current[i] = min(current[i], current[i-sq]+1)
        return current[-1]
