class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        L = 0
        R = 0

        for c in s1:
            if c not in count1:
                count1[c] = 1
            else:
                count1[c] += 1
        
        for R in range(len(s2)):
            if s2[R] not in count2:
                count2[s2[R]] = 1
            else:
                count2[s2[R]] += 1
            if (R - L + 1) > len(s1):
                count2[s2[L]] -= 1
                if count2[s2[L]] == 0:
                    del count2[s2[L]]
                L += 1
            if count2 == count1:
                return True
        return False
            
        