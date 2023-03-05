class Solution:
    def romanToInt(self, s: str) -> int:
        sym={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val=0
        temp=1000
        for i in range(len(s)):
            val=val+sym[s[i]]
            if sym[s[i]] > temp:
                val= val-2*temp
            temp=sym[s[i]]
        return val
        


