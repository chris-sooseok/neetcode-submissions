class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        
        h, t = 0, len(cleaned) - 1

        while h < t:
            if cleaned[h] != cleaned[t]:
                return False
            h += 1
            t -= 1
        
        return True
