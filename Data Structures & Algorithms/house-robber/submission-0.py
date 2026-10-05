class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:                 # only one house → rob it
            return nums[0]

        dp = [0] * len(nums)               # dp[i] = most money from houses 0..i
        dp[0] = nums[0]                    # base: one house
        dp[1] = max(nums[0], nums[1])      # base: two houses, take the richer

        for i in range(2, len(nums)):      # range moves i for you
            skip = dp[i - 1]               # don't rob house i
            rob = nums[i] + dp[i - 2]      # rob house i, so skip i - 1
            dp[i] = max(skip, rob)
        return dp[-1]                      # best using all the houses
        