class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans=0
        dd=dividend if dividend>=0 else -1*dividend
        ds=divisor if divisor>=0 else -1*divisor
        ans=len(range(dd+1,0,-ds))-1
        if dd==ds:
            ans=1
        if ((dividend >=0 and divisor>=0) or (dividend<=0 and divisor<=0)) and ans <= 2**31-1:
            return ans
        if ((dividend >=0 and divisor>=0) or (dividend<=0 and divisor<=0)) and ans > 2**31-1:
            return 2**31-1
        if ((dividend >=0 and divisor<=0) or (dividend<=0 and divisor>=0)) and ans <= 2**31:
            return -1*ans
        if ((dividend >=0 and divisor<=0) or (dividend<=0 and divisor>=0)) and ans > 2**31:
            return -1*(2**31)
