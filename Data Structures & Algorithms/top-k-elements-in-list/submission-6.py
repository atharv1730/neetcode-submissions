class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First get the count of all the elements
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Push in heap of size k
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Return elements
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result