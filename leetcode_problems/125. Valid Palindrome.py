class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for c in s:
            if ord(c)>64 and ord(c)<91:
                string += c
            if ord(c)>96 and ord(c)<123:
                string += chr(ord(c)-32)
            if ord(c)>47 and ord(c)<58:
                string += c
        for i in range(len(string)):
            if string[i]!=string[len(string)-1-i]:
                return False
        return True
