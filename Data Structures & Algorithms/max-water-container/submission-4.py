class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        result = 0

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            result = max(result, area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return result

        