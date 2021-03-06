from collections import deque

class Solution:
    def reconstructQueue(self, people):
        """O(n^2) time | O(n) space"""
        people = sorted(people, key=lambda x: [-x[0], x[1]])
        result = []
        for person in people:
            result.insert(person[1], person)
        return result
