class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for w in strs:
            wl = len(w)
            encoded += str(len(w)) + "#" + w
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        l = len(s)
        i = 0
        while i < len(s):
            j = s.index("#", i)
            ls = int(s[i:j])
            decoded.append(s[j + 1:ls+ j + 1])
            i = ls + 1 + j
        return decoded
            
