class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # if len(nums)<3:
        #     return -1
        # nums.remove(max(nums))
        # nums.remove(min(nums))
        # return(nums[0])
        return -1 if len(nums) < 3 else sum(nums[:3]) - min(nums[:3]) - max(nums[:3])
