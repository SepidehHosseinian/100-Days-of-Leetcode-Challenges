class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zero, l = 0, 0
        for r, n in enumerate(nums):
            zero += n == 0
            if zero > k:
                zero -= nums[l] == 0
                l+=1
        return r - l + 1
