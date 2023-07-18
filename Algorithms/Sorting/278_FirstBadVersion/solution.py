# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool: pass

class Solution:
    

    def firstBadVersion(self, n: int) -> int:
        # initialize the left and right pointers
        left = 1
        right = n
        # loop until the range is empty
        while left <= right:
        # find the middle version
            mid = (left + right) // 2
            # check if it is bad
            if isBadVersion(mid):
            # if it is bad, the first bad version is in the left half
                right = mid - 1
            else:
            # if it is good, the first bad version is in the right half
                left = mid + 1
        # return the left pointer as the first bad version
        return left