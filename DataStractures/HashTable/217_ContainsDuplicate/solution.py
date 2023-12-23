from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = list(set(nums))
        return not (len(numSet) == len(nums))
    #217