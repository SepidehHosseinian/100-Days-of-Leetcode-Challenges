class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
  
##Soltion one:##

#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if 2*arr[j]==arr[i] and i!=j:
#                     return True
#        else:
#            return False
                

##Solution Two:##
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2) != i:
                return True
        return False



##Solution Three#
        # arr.sort()
        # for i in range(len(arr)):
        #     product = arr[i]*2
        #     lo,hi = 0,len(arr)-1
        #     while lo<=hi:
        #         mid = (lo+hi)//2
        #         if arr[mid]==product and mid!= i:
        #             return True
        #         elif arr[mid]<product:
        #             lo+=1
        #         else:
        #             hi-=1
        # return False