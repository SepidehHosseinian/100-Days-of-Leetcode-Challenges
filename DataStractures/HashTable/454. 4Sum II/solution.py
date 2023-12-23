from ast import List
from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        lookup = defaultdict(int)
        counter = 0
        
        for i in nums1:
            for j in nums2:
                count = i+j
                lookup[count]+= 1
                
        for k in nums3:
            for l in nums4:
                count = -(k+l)
                if count in lookup:
                    counter += lookup[count]
        return counter