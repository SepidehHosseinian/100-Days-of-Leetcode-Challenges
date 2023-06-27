from ast import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         lookup = {i:[list1.index(i)] for i in list1}
#         for j in list2:
#             if j in lookup:
#                 lookup[j].append(list2.index(j))
                
#         temp = []
#         min_idx = 2000

#         for k, v in lookup.items():
#             if len(lookup[k])==1:
#                 lookup[k]= [2000]
#             elif len(lookup[k])>1:
#                 sum_idx = sum(i for i in lookup[k])
#                 min_idx = min(sum_idx, min_idx)
#         for k,v in lookup.items():
#              if sum(i for i in lookup[k])==min_idx:
#                     temp.append(k)            
#         return temp
    
        acc_len = len(list1)+len(list2)
        lookup = {}
        for word in list1:
            if word in list2:
                length = list1.index(word) + list2.index(word)
                acc_len= min(acc_len, length)
                lookup[word]= length
        
        result = []
        for k,v in lookup.items():
            if v == acc_len:
                result.append(k)
        return result
    #599