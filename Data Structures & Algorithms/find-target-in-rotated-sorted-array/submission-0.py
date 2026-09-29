class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[L] <= nums[mid]: #left half is sorted since L is smaller than mid
                if target >= nums[L] and target < nums[mid]: 
                    R = mid - 1
                else:
                    L = mid + 1
            elif nums[R] >= nums[mid]: 
                if target > nums[mid] and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1