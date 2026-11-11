class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        match = {'(': ')', '[': ']', '{':'}'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if char != match[prev]:
                    return False
        
        # if anything is left, false
        if stack:
            return False

        return True