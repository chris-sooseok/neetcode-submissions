class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sc = {}
        tc = {}

        for c1, c2 in zip(s, t):
            sc[c1] = 1 + sc.get(c1, 0)
            tc[c2] = 1 + tc.get(c2, 0)
        
        return sc == tc