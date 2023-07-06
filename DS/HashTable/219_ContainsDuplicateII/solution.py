from ast import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen={}
        for idx,x  in enumerate(nums):
                
                if x in seen and idx - seen[x]<=k:
                    return True
                else:
                    seen[x]=idx
        #219