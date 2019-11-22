def minAddToMakeValid(self, string):
    """O(n) time and space"""
    stack = []
    for char in string:
        if stack and char == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

def minAddToMakeValid(self, string):
    """O(n) time | O(1) space"""
    not_closed = 0
    brackets = 0
    for char in string:
        if char == ")":
            if brackets <= 0:
                not_closed += 1
            else:
                brackets -= 1
        else:
            brackets += 1
    return not_closed + brackets
