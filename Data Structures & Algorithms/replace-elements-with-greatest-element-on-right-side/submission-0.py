class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        for i in reversed(range(0, len(arr) - 1)):
            prev = greatest
            greatest = max(arr[i], greatest)
            arr[i] = prev
        arr[-1] = -1
        return arr