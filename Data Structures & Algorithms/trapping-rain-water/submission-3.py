class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxLeft = 0
        maxRight = 0
        result = 0  

        while L < R:
            if height[L] <= height[R]:
                # process left side
                maxLeft = max(maxLeft, height[L])
                result += maxLeft - height[L]
                L += 1
            else:
                # process right side
                maxRight = max(maxRight, height[R])
                result += maxRight - height[R]
                R -= 1
        return result
