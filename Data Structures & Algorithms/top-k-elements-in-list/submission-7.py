class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        x = []
        for num, count in counts.items():
            x.append([count, num])

        x.sort()

        result = []
        while len(result) < k:
            result.append(x.pop()[1])
        
        return result