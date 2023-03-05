class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out=0
        for i in range(len(columnTitle)):
            out += (ord(columnTitle[len(columnTitle)-1-i])-64)*(26**i)
        return out
