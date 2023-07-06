from ast import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numset1, numset2 = set(nums1), set(nums2)
        return(numset1.intersection(numset2))
    #349