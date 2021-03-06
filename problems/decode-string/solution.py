class Solution:
    def decodeString(self, s: str) -> str:
        """O(n) time and space"""
        return solve(0, s)

def solve(i, string):
    result = []
    while i < len(string):
        char = string[i]
        if char.isnumeric():
            multiplier = []
            while string[i].isnumeric():
                multiplier.append(string[i])
                i += 1
            multiplier = int(''.join(multiplier))
            word, i = solve(i+1, string)
            result.append(word * multiplier)
        elif string[i] == ']':
            return (''.join(result), i+1)
        else:
            result.append(string[i])
            i += 1
    return ''.join(result)
