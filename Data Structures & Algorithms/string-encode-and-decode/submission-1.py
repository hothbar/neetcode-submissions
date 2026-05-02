class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for w in strs:
            output += w + "é"
        return output

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        for char in s:
            if char == "é":
                res.append(cur)
                cur = ""
                continue
            cur += char
        return res
