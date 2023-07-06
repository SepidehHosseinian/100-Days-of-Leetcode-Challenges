class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        lookup = {" ":" "}
        i = 0
        ans  = ""
        alphabets = 'abcdefghijklmnopqrstuvwxyz'

        for char in key:
            if char not in lookup:
                lookup[char] = alphabets[i]
                i += 1
        
        for char in message:
            ans += lookup[char]

        return ans