class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(left, right):              # is the piece from left to right a palindrome?
            while left < right:
                if s[left] != s[right]:      # ends don't match
                    return False
                left += 1                    # move inward
                right -= 1
            return True                      # every pair matched

        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] == s[R]:                 # match → keep going
                L += 1
                R -= 1
            else:                            # mismatch → try deleting each one
                return isPal(L + 1, R) or isPal(L, R - 1)
        return True                          # never mismatched → already a palindrome