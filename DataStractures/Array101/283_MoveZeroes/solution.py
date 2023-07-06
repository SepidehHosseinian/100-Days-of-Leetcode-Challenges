class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
#         nums_zeros = nums.count(0)        
#         for i in range(nums_zeros):
#             nums.remove(0)
#             nums.append(0)
            
            
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        