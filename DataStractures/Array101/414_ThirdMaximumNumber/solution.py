class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        nums2= set(nums)
        nums2= sorted(nums2)
        
        if len(nums2)>=3:
            return nums2[-3]
        else:
            return max(nums)
        