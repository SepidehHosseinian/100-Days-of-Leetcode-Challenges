class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        top=len(needle)
        for i in range(len(haystack)):
            if haystack[i:top+i]==needle:
                return i
        else:
            return -1
        #28
