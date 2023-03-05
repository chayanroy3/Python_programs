class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        l=len(digits)
        i=1
        while c>0 and l-i>=0:
            a=digits[l-i]+1
            digits[l-i] = int(a%10)
            c=int(a/10)
            i=i+1
        if l-i<0 and c>0:
            digits.insert(0,1)
        return digits


       
