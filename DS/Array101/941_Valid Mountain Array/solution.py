class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        
        if len(arr)<3:
            return False
                
        peak=arr.index(max(arr))    
        
        if peak == 0 or peak == len(arr) - 1:
            return False
        else:
            result = True
            for i in range(0, peak):
                if arr[i] >= arr[i + 1]:
                    result = False
                    break
            
            
            if result:
                for k in range(peak+1, len(arr)):
                        
                    if arr[k - 1] <= arr[k]:
                        return False
                    
            else:
                return False
                        
        return True