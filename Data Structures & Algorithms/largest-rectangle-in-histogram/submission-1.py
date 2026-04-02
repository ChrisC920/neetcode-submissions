class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left_limits = [-1] * len(heights)
        right_limits = [len(heights)] * len(heights)

        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left_limits[i] = -1 if not stack else stack[-1]
            stack.append(i)
        stack.clear()
        for i in reversed(range(len(heights))):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right_limits[i] = len(heights) if not stack else stack[-1]
            stack.append(i)
        print(left_limits)
        print(right_limits)
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (right_limits[i] - left_limits[i] - 1))
        return res