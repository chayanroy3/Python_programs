class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=1
        for a in nums2:
            nums1[-i]=a
            i=i+1
        nums1.sort()
