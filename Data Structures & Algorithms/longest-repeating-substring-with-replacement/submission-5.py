class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        maxCount = 0
        myHash = {}
        result = 0

        for R in range(len(s)):
            if s[R] not in myHash:
                myHash[s[R]] = 1
            else:
                myHash[s[R]] += 1
            maxCount = max(maxCount, myHash[s[R]])
            while (R - L + 1) - maxCount > k:
                myHash[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)
        return result