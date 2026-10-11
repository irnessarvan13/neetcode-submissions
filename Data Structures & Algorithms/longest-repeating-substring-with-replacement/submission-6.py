class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myHash = {}
        L = 0
        result = 0

        for R in range(len(s)):
            if s[R] not in myHash:
                myHash[s[R]] = 1
            else:
                myHash[s[R]] += 1
            while (R - L + 1) - max(myHash.values()) > k:
                myHash[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)
        return result
