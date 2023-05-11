class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons_cnt=0
        one_counter=0
        for i in nums:
            if i ==1:
                one_counter += 1
                cons_cnt = max(cons_cnt, one_counter)
            else: one_counter = 0
        return cons_cnt
                