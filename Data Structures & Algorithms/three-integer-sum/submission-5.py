class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                     # sort so two pointers work (smaller left, bigger right)
        result = []                     # every triplet that adds to 0

        for i in range(len(nums)):      # lock in the first number of the triplet
            # skip duplicate nums — same first number = same triplets as last time
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1                   # left pointer starts right after the locked number
            R = len(nums) - 1           # right pointer starts at the end

            while L < R:                # Two Sum II on everything after i
                total = nums[i] + nums[L] + nums[R]
                if total > 0:
                    R -= 1              # too big → move to a smaller number
                elif total < 0:
                    L += 1              # too small → move to a bigger number
                else:
                    result.append([nums[i], nums[L], nums[R]])   # found one, save it
                    L += 1              # move on to look for more
                    # skip repeat L values so the same triplet isn't added twice
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return result                   # all unique triplets

        
