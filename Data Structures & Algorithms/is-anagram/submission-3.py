class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}

        for val in s:
            if val not in string1:
                string1[val] = 1
            else:
                string1[val] += 1
        
        for val in t:
            if val not in string2:
                string2[val] = 1
            else:
                string2[val] += 1

        if string1 != string2:
            return False
        else:
            return True