class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            i= n%2
            if i==1:
                count+=1
            n=n//2
        return count
