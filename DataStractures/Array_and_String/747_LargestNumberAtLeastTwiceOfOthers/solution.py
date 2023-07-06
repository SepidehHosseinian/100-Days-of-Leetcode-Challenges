class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m = max(nums)
        i = nums.index(m)
        nums.remove(m)
        if 2*max(nums) <= m :
            return i
        return -1