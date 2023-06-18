class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        N = len(nums)
        LIS = [1] * N
        LDS = [1] * N

        # Longest Increasing Subsequences from Left
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        #Longest Increasing Subsequences from Right
        for i in range(N-1,-1,-1):
            for j in range(i+1, N):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], 1 + LDS[j])
        
        ans = 1000
        for a,b in zip(LIS, LDS):
            if a == 1 or b == 1: continue
            else: ans = min(ans, N - a - b + 1)
        return ans
