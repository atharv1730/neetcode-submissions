class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_s, char_t = {}, {}
        for i in s:
            char_s[i] = char_s.get(i, 0) + 1
        for i in t:
            char_t[i] = char_t.get(i, 0) + 1

        return char_s == char_t