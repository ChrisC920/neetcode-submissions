class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] * (r - l) > max_area:
                    max_area = heights[l] * (r - l)
                l += 1
            else:
                if heights[r] * (r - l) > max_area:
                    max_area = heights[r] * (r - l)
                r -= 1
        return max_area