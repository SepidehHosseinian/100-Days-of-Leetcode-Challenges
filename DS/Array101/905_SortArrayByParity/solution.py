class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        
        if len(nums)==1:
            return nums
        
        else:
            n=0
            for i in range(len(nums)):
                if nums[i]%2==0:
                    nums[n], nums[i]=nums[i], nums[n]
                    n +=1
            return nums
                
                    