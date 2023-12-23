from ast import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = Counter(nums).most_common()
        return s[-1][0]
    #136
        