class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:


        #Solution 01
        #         countGlobal=0
        #         countCurrent=0

        #         for i in range (len(nums)):

        #             if nums[i]==1:
        #                 countCurrent +=1
        #                 countGlobal=max(countGlobal, countCurrent)

        #             else:

        #                 countCurrent=0

        #         return countGlobal

        #        return len(max("".join(map(str, nums)).split("0")))


        #Solution 02
        c = 0
        a = []
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1

            else:
                a.append(c)
                c = 0
        a.append(c)
        return max(a)
    
        ##Solution 03
        # consecutive = result = 0
        # for n in nums:
        #     consecutive = consecutive*n+n
        #     result = max(result, consecutive)
        # return result

        #Solution 04
        # cons_cnt=0
        # one_counter=0
        # for i in nums:
        #     if i ==1:
        #         one_counter += 1
        #         cons_cnt = max(cons_cnt, one_counter)
        #     else: one_counter = 0
        # return cons_cnt
