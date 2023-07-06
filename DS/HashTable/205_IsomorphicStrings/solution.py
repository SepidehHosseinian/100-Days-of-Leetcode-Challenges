class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Approach01
        hashmap = {}
        for i , j in zip(s, t):
            if i in hashmap:
                if hashmap[i]!=j:
                    return False
            elif j in hashmap.values():
                return False
            else:
                hashmap[i]= j
            
        return True
    
        #Approach 02
        # m1 = [s.index(i) for i in s]
        # m2 = [t.index(i)for i in t]
        # print(m1, m2)
        # return m1==m2
        #205