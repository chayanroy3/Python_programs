class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=dict()
        for i in range(len(nums)):
            another= target- nums[i]
            if another in temp:
                return [temp[another],i]
            temp[nums[i]]=i
                
