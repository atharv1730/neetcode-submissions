class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for n in strs:
            result.append(str(len(n)) + "#" + n)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res

