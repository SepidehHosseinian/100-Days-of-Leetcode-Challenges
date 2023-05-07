class Solution:
    def duplicateZeros(self, arr:list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        res=[]
        for i in range(len(arr)):
            if arr[i] == 0 :
                res.append(0)
                res.append(0)
                
            else:
                res.append(arr[i])
                   
        
       
        m = len(res)
        for i in range(m-n):
            res.pop()
            