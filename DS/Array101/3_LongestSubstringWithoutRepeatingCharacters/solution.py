class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        i=0
        count = 0

        if len(s)==1:
            return 1
        else:
            while i < len(s):
                if s[i] not in ans:
                    ans += s[i]   
                else:
                    ans  = ans[(ans.index(s[i])+1):]+ s[i]   
                i +=1
                count = max(count, len(ans))    
            return(count)
            #3
