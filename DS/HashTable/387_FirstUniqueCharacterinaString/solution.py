from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)<=0: return -1
        occurence_map=Counter(list(s))
        print(occurence_map)
        for k,v in occurence_map.items():
            if v==1 :return s.index(k)
            
        return -1