class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #approach 01
#         while val in nums:
#             nums.pop(nums.index(val))
            
#         return(len(nums))
    
        #approach 02
        # while val in nums: nums.remove(val)
    
        #approach 03
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x 
                i += 1
        return i
