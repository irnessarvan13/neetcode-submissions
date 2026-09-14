class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for val in s:
            if val not in hash1:
                hash1[val] = 1
            else:
                hash1[val] += 1
        
        for val in t:
            if val not in hash2:
                hash2[val] = 1
            else:
                hash2[val] += 1

        return hash1 == hash2