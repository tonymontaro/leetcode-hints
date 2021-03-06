from collections import deque

class Solution:
    def deckRevealedIncreasing(self, cards):
        """O(nlogn) time | O(n) space"""
        cards.sort()
        indexes = deque(range(len(cards)))
        result = [0] * len(cards)
        for card in cards:
            result[indexes.popleft()] = card
            if indexes:
                indexes.append(indexes.popleft())
        return result
