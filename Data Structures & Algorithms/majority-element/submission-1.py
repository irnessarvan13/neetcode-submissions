class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myHash = {}

        for num in nums:
            if num not in myHash:
                myHash[num] = 1
            else:
                myHash[num] += 1

            maxVal = max(myHash, key=myHash.get)
        return maxVal

        