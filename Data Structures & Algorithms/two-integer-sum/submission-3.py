class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}

        for i, num in enumerate(nums):
            if target - num in myHash:
                return [myHash[target - num], i]
            else:
                myHash[num] = i
        return myHash
        