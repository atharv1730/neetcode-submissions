class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            sorted_word = ''.join(sorted(i))
            result[sorted_word].append(i)

        return list(result.values())