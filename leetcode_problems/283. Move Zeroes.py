class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        init=False
        for i in range(len(nums)):
            if init==False and nums[i]==0:
                j=i
                init=True
            if init==True and nums[i]!=0:
                nums[j]=nums[i]
                nums[i]=0
                j+=1
