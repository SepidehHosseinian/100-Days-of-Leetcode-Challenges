class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        #1
        # max_init = -1
        # for i in range(len(nums)):
        #     if -nums[i] in (nums):
        #         max_init = max(max_init, abs(nums[i]))
        # return max_init 
        #2
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
        #3
        # return max([-1] + [x for x in nums if x > 0 and -x in nums])    
