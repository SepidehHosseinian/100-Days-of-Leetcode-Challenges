class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        visited = {} # hash map of most recent position of each character that has appeared
        start = longest = 0
        for i, char in enumerate(s):
            if char in visited: 
                start = max(start, visited[char] + 1)
            visited[char] = i
            longest = max(longest, i - start + 1)
        return longest