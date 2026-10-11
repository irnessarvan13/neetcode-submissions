class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L = 0

        for R in range(len(t)):
            if L < len(s) and s[L] == t[R]:
                L += 1
        return L == len(s)

