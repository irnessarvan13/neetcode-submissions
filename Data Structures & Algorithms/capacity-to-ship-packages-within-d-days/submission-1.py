class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L = max(weights)
        R = sum(weights)

        while L <= R:
            mid = (L + R) // 2

            needed = 1
            total = 0

            for weight in weights:
                if total + weight > mid:
                    needed += 1
                    total = 0
                total += weight

            if needed <= days:
                R = mid - 1
            else:
                L = mid + 1
        return L
