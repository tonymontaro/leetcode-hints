class Solution:
    def dailyTemperatures(self, arr):
        """O(n) time and space"""
        result = [0] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and stack[-1][0] < arr[i]:
                temp = stack.pop()
                result[temp[1]] = i - temp[1]
            stack.append([arr[i], i])
        return result
