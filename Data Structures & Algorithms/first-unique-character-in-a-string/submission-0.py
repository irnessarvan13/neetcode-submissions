class Solution:
    def firstUniqChar(self, s: str) -> int:
        myHash = {}

        for i, num in enumerate(s):
            if num not in myHash:
                myHash[num] = 1
            else:
                myHash[num] += 1
        
        for i, num in enumerate(s):
            if myHash[num] == 1:
                return i
        return -1
            
        