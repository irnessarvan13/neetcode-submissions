class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:                  # 1 step → 1 way, 2 steps → 2 ways
            return n

        dp = [0] * (n + 1)          # dp[i] = ways to reach step i (size n+1 so index n exists)
        dp[1] = 1                   # base case
        dp[2] = 2                   # base case

        for i in range(3, n + 1):   # range stops BEFORE n+1, so this includes n
            dp[i] = dp[i - 1] + dp[i - 2]   # came from 1 step below, or 2 steps below
        return dp[n]