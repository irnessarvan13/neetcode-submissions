class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count = []

        for num in nums:
            if num not in count:
                count.append(num)
            else:
                return True
        return False
        