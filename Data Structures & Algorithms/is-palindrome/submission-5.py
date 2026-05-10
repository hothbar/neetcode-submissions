class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            print(s[l])
            print(s[r])

            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    print(s[l])
                    print(s[r])
                    return False
                else:
                    #print(s[l])
                    #print(s[r])
                    l += 1
                    r -= 1
            else:
                if not s[l].isalnum():
                    print(s[l])
                    l += 1
                if not s[r].isalnum():
                    print(s[r])
                    r -= 1
                    
        return True
        