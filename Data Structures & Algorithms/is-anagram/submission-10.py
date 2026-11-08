class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ht1 = {}
        ht2 = {}

        for c in s:
            if c not in ht1:
                ht1[c] = 1
            else:
                ht1[c] += 1

        for c in t:
            if c not in ht2:
                ht2[c] = 1
            else:
                ht2[c] += 1

        return ht1 == ht2

            
        
        