class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
            else:
                continue

        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append( 0)
        return nums
