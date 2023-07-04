from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,  len(nums)-1
        target_sum=0
        while l < r:
            target_sum = (nums[l]+nums[r])
            if target_sum==target:
                return (l+1,r+1)
            elif target_sum<target:
                l+=1
            else: 
                r-= 1
        #167
        
