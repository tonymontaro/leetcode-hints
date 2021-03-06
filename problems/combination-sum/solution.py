class Solution(object):
    def combinationSum(self, candidates, target):
        return self.helper(candidates, target, [], set())
    
    def helper(self, arr, target, comb, result):
        for num in arr:
            if target - num == 0:
                result.add(tuple(sorted(comb[:] + [num])))
            elif target - num > 0:
                self.helper(arr, target-num, comb[:]+[num], result)
        return result
