from ast import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l,r = 0,  1
        max_sum=0
        while r < (len(nums)):
            max_sum += min(nums[l], nums[r])
            l+= 2
            r+= 2
        return max_sum
        #approach2
        #return sum(sorted(nums)[::2])
    #561
