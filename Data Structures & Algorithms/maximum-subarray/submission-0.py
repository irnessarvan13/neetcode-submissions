class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        best = nums[0]

        for num in nums:
            if current < 0:
                current = num
            else:
                current += num
            best = max(best, current)
        return best

