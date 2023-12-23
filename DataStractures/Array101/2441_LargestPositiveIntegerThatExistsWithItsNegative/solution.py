from ast import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        #Approach 01
        # max_init = -1
        # for i in range(len(nums)):
        #     if -nums[i] in (nums):
        #         max_init = max(max_init, abs(nums[i]))
        # return max_init 
        #Approach 02
        dict1 = {}
        res = []
        for i in nums :
            if abs(i) in dict1.keys() :
                if dict1[abs(i)] + i == 0 :
                    res.append(abs(i))
            else:
                dict1.update({abs(i) : i})
        if res : 
            return max(res)
        else : 
            return -1
        #Approach 03
        # return max([-1] + [x for x in nums if x > 0 and -x in nums])    
