class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(sorted(s))
        s2 = list(sorted(t))

        if s1 == s2:
            return True
        else:
            return False
        