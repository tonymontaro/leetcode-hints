class Solution:
    def search(self, arr, target) -> int:
        """O(logn) time | O(1) space"""
        l, h = 0, len(arr)-1
        while l <= h:
            mid = (l+h)//2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                if arr[l] <= target or arr[l] > arr[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if arr[h] >= target or arr[h] < arr[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
