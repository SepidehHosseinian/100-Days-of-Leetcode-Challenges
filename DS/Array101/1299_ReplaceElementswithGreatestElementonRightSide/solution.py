class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # max= arr[len(arr)-1]
        # for i in range (len(arr)-1, -1, -1):
        #     if i == len(arr)-1:
        #         arr[i]=-1
        #     else:
        #         temp= arr[i]
        #         arr[i]=max
        #         if temp>max:
        #             max=temp
        # return arr
        #Approach 02
        me,arr[-1] = arr[-1],-1
        
        for i in range(len(arr)-2,-1,-1):
            arr[i],me = me,max(me,arr[i])
            
        return arr
        
