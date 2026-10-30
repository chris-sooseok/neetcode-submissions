import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded
    def decode(self, s: str) -> List[str]:

        decoded = []
        n = len(s)
        i = 0
        length = "" # must be string to append number char

        while i < n:
            # check if int
            # if so, append char and advance
            if s[i].isdigit():
                length += s[i]
                i += 1
            
            # otherwise, it is #
            # read the string and append it
            # then advance i
            elif s[i] == "#":
                decoded.append(s[i+1:i+1+int(length)])
                i += int(length) + 1
                # reset length, so next string can be read
                length = ""

        return decoded