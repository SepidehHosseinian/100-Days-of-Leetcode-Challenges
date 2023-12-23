class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #Approach 01
#         jewel_l = [i for i in jewels]
#         stone_l = [i for i in stones]
#         counter = 0
        
#         for i in stone_l:
#             if i in jewel_l:
#                 counter +=1
#             else:
#                 continue
#         return counter
        #Approach 02
        lookup_jewel = {i:0 for i in jewels}
        for i in stones:
            if i in lookup_jewel.keys():
                lookup_jewel[i] +=1
            
        return(sum(lookup_jewel.values()))
       ## return sum(Counter(stones)[i] for i in jewels)