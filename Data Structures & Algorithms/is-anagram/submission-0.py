class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sc = {}
        tc = {}

        for c1, c2 in zip(s, t):
            if c1 in sc:
                sc[c1] += 1
            else:
                sc[c1] = 1
            
            if c2 in tc:
                tc[c2] += 1
            else:
                tc[c2] = 1
        
        if sc != tc:
            return False
        else:
            return True