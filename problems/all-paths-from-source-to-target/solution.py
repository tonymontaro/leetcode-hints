class Solution(object):
    """O(N*D)?"""
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        return solve(target, 0, graph, [], [])

def solve(target, i, arr, prev=[], res=[]):
    prev.append(i)
    if i == target:
        res.append(prev)
    else:
        for j in arr[i]:
            solve(target, j, arr, list(prev), res)
    return res
