class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)   # convert to set for O(1) lookup + remove duplicates
        longest = 0         # track the longest sequence found so far

        for num in nums:
            if num - 1 not in mySet:    # only start counting if this is a sequence START
                length = 1              # current sequence length starts at 1
                while num + length in mySet:    # keep counting while next number exists
                    length += 1         # increment sequence length
                longest = max(longest, length)  # update best if current is longer
        return longest      # return the longest sequence found