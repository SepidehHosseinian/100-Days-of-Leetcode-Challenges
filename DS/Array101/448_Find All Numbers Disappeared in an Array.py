class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
#         n=len(nums)               
#         return [i for i in range(1,n+1) if i not in nums]
#Time Complexity O(n**2)

        s= set(nums)
        return[i for i in range(1,len(nums)+1) if i not in s]
#Time Complexity O(n)
        