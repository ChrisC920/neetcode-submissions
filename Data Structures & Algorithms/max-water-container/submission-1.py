class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftBounds = [0] * len(heights)
        rightBounds = [0] * len(heights)
        leftBounds[0] = heights[0]
        rightBounds[len(heights) - 1] = heights[len(heights) - 1]
        for i in range(1, len(heights)):
            leftBounds[i] = max(leftBounds[i - 1], heights[i])
            rightBounds[len(heights) - 1 - i] = max(rightBounds[len(heights) - i], heights[len(heights) - 1 - i])
        print(leftBounds)
        print(rightBounds)
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(leftBounds[l], rightBounds[r])
            print(f"{area} {l} {r}")
            res = max(area, res)
            if leftBounds[l] <= rightBounds[r]:
                l += 1
            else:
                r -= 1
        return res