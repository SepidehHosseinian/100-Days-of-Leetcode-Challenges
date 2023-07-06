from ast import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map=Counter(list(nums1))
        nums2_map=Counter(list(nums2))
        res=nums1_map & nums2_map
        return res.elements()
    #350