class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        arr2=[]
        
        for i in range(len(arr)):
            if arr[i]==0:
                arr2.append(i)
                
        k=0
        for i in range(len(arr2)):
            arr.insert(arr2[i]+k, 0)
            k +=1
            
        m= len(arr)
        for i in range(m-n):
            arr.pop()
            
        return arr
    #Approach 02
        # i = 0
        # while i<len(arr):
        #     if arr[i]==0:
        #         arr.insert(i+1, 0)
        #         arr.pop()
        #         i +=1
        #     i +=1
            
        # return arr
