class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        while l < r:
            if max_left < max_right:
                l += 1
                val = max_left - height[l]
                total += val if val >= 0 else 0
                max_left = max(max_left, height[l])
            else:
                r -= 1
                val = max_right - height[r]
                total += val if val >= 0 else 0
                max_right = max(max_right, height[r])

        return total