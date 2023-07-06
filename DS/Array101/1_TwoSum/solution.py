class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j]+nums[i]==target:
                    return[i,j]

        #approach 02
        # seen ={}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in seen:
        #         return[seen[diff], i]
        #     else:
        #         seen[nums[i]] = i
