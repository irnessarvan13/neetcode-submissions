class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        count = 0
        total = 0

        for num in nums:
            total += num
            need = total - k
            if need in seen:
                count += seen[need]
            if total not in seen:
                seen[total] = 1
            else:
                seen[total] += 1
        return count  

            