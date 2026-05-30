class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        gram = True
        if len(s) != len(t):
            gram = False
        
        for i in set(s):
            if i not in t or s.count(i) != t.count(i):
                gram = False

        return gram