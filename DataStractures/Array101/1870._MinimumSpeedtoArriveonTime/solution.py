from ast import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour): return -1

        def isEnoughSpeed(s):
            return sum(ceil(d/s) if i != L else d/s for i, d in enumerate(dist)) <= hour

        l, r, L = 1, 10**7, len(dist)-1
        
        while l < r:
            speed = (l+r)//2
            if isEnoughSpeed(speed):
                r = speed
            else:
                l = speed + 1
        
        return l