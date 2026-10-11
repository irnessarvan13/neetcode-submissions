class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        count1 = {}
        count2 = {}

        for val in s1:
            if val not in count1:
                count1[val] = 1
            else:
                count1[val] += 1

        for R in range(len(s2)):
            if s2[R] not in count2:
                count2[s2[R]] = 1
            else:
                count2[s2[R]] += 1
            while (R - L + 1) > len(s1):
                count2[s2[L]] -= 1
                if count2[s2[L]] == 0:
                    del count2[s2[L]]
                L += 1
            if count1 == count2:
                return True
        return False
