import collections

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        #Approach01
        # create count dic
        count = collections.Counter(s)
        
        # any char is not enough
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        # sliding window
        res = len(s)
        l = 0
        for r in range(len(s)):
            # update count
            count[s[r]] -= 1
            # if freq not enough for the remaining string
            while l <= r and (count['a'] < k or count['b'] < k or count['c'] < k):
                count[s[l]] += 1
                l += 1
            # update valid res
            res = min(res, count['a'] + count['b'] + count['c'])
        return res

        #Approach 02
        # limits = {c: s.count(c) - k for c in 'abc'}
        # if any(x < 0 for x in limits.values()):
        #     return -1

        # cnts = {c: 0 for c in 'abc'}
        # ans = l = 0
        # for r, c in enumerate(s):
        #     cnts[c] += 1
        #     while cnts[c] > limits[c]:
        #         cnts[s[l]] -= 1
        #         l += 1
        #     ans = max(ans, r - l + 1)

        # return len(s) - ans
