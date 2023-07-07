from collections import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 01
        #counter = 0
        #while n != 0:
         #   if n & 1 ==1:
          #      counter +=1
           # n = n >> 1
        #return counter
        # Approach 02
        counter = Counter(bin(n)[2:])
        return counter.get("1", 0)