class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myHash = {}

        for val in strs:
            key = ''.join(sorted(val))
            if key not in myHash:
                myHash[key] = []
            myHash[key].append(val)
        return list(myHash.values())

