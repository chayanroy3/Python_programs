class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        return int((n*(n+1)/2)-s)
