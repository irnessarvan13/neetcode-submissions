class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):                 # blank 1: every number has been decided
                result.append(subset.copy())  # blank 2: save a SNAPSHOT
                return

            subset.append(nums[i])     # TAKE nums[i]
            backtrack(i + 1)
            subset.pop()               # blank 3: UNDO the take
            backtrack(i + 1)           # SKIP nums[i]

        backtrack(0)
        return result