class Solution:
    def isValid(self, s: str) -> bool:
        mapped = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in mapped:
                if stack and stack[-1] == mapped[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
        