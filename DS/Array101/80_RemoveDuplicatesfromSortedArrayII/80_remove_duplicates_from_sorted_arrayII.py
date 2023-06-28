class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #Approch 01
        # nums_count={c: nums.count(c) for c in nums}
        # nums.clear()
        # for k, v in nums_count.items():
        #     if v>=2:
        #         nums.append(k)
        #         nums.append(k)
        #     else:
        #         nums.append(k)
        # return(len(nums))
        
        #Approach 02
        i = 1
        while (i<len(nums)-1):
            if (nums[i-1]==nums[i] and nums[i]==nums[i+1]):
                nums.pop(i)
            else:
                i +=1
        return (len(nums))
