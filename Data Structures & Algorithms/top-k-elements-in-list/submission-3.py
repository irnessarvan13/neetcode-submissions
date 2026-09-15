class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = {}
        heap = []

        for num in nums:
            if num not in myHash:
                myHash[num] = 1
            else:
                myHash[num] += 1
        
        for num, count in myHash.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
 