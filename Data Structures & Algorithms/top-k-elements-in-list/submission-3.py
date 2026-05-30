class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        bucket = [[] for x in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for n in bucket[i]:
                    result.append(n)
                    if len(result) == k:
                        return result
