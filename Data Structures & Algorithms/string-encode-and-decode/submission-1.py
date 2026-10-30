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

        while i < n:
            j = s.index("#", i)
            length = s[i:j]
            decoded.append(s[j+1 : j+1+ int(length)])
            i += len(length) + 1 + int(length)

        return decoded