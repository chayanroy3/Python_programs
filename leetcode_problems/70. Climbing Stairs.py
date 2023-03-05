class Solution:
    def climbStairs(self, n: int) -> int:
        t=0
        f0=1
        for i in range(0,n):
            f1=f0+t
            t=f0
            f0=f1
        return f1
