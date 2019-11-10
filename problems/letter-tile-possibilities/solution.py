# not the best solution
from collections import Counter

class Solution(object):
    """O(N*U) time | O(N) space | N -> len of tiles, U -> len of unique characters"""
    def numTilePossibilities(self, tiles):
        return tile_possibilities(Counter(tiles))

def tile_possibilities(counts):
    total = 0
    for key in counts.keys():
        if counts[key] > 0:
            new_counts = dict(counts)
            new_counts[key] -= 1
            total += 1 + tile_possibilities(new_counts)
    return total
