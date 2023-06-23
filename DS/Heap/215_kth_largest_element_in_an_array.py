
from ast import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        maxheap, res = [], None
        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            res = -heapq.heappop(maxheap)
        return res
