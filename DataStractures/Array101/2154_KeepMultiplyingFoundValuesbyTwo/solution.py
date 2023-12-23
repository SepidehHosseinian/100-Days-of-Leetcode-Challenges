from ast import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original = original*2
        else:
            return original
    #2154
