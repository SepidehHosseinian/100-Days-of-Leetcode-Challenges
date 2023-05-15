class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        max= arr[len(arr)-1]

        for i in range (len(arr)-1, -1, -1):
            if i == len(arr)-1:
                arr[i]=-1
            else:
                temp= arr[i]
                arr[i]=max
                if temp>max:
                    max=temp
        return arr