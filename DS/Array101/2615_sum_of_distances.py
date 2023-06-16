class Solution:
    def distance(self, nums: list[int]) -> list[int]:

        mp=defaultdict(list)
        for i,j in enumerate(nums):
            mp[j].append(i)
        
        ans=[0]*len(nums)
        for k,v in mp.items():
            perfix_sum=0
            perfix_len=0
            suffix_sum=sum(v)
            suffix_len=len(v)
            for i in v :
                perfix_sum+=i
                perfix_len+=1
                suffix_sum-=i
                suffix_len-=1
                ans[i]=(-perfix_sum+perfix_len*i-suffix_len*i+suffix_sum)
        return ans
