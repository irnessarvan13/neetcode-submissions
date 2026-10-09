class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myHash = {}
        best = 0
        bestCount = 0

        for num in nums:
            if num not in myHash:
                myHash[num] = 1
            else:
                myHash[num] += 1

        for num, count in myHash.items():
            if count > bestCount:
                best = num
                bestCount = count
        return best

        