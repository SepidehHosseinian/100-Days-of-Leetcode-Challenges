from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(Counter(stones)[i] for i in jewels)