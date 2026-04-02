class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        # Find max left and max right arrays
        max_lefts = [0] * len(height)
        max_rights = [0] * len(height)
        for i in range(0, len(height) - 1):
            right_index = len(height) - i - 1
            max_lefts[i + 1] = max(max_lefts[i], height[i])
            max_rights[right_index - 1] = max(max_rights[right_index], height[right_index])

        for i in range(len(height)):
            val = min(max_lefts[i], max_rights[i]) - height[i]
            total += val if val >= 0 else 0
        print(max_lefts)
        print(max_rights)
        return total