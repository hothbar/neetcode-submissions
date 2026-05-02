class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        lw, la = len(word), len(abbr)
        i = j = 0
        
        while i < lw and j < la:
            if abbr[j] == '0':
                return False
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            elif abbr[j].isalpha():
                return False
            else:
                sl = 0
                while j < la and abbr[j].isdigit():
                    sl = sl * 10 + int(abbr[j])
                    j += 1
                i += sl
        return i == lw and j == la
        