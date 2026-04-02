class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (starting index, height)
        largest = heights[0]

        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                continue
            if stack[-1][1] > h:
                while stack and stack[-1][1] > h:
                    largest = max(largest, (i - stack[-1][0]) * stack[-1][1])
                    lastI, lastH = stack.pop()
                stack.append((lastI, h))
            else:
                stack.append((i, h))
        for s in stack:
            largest = max(largest, (len(heights) - s[0]) * s[1])
        return largest