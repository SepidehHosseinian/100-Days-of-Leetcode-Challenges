class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # odds=[]
        # evens=[]
        # answer=[]
        # for i in range(len(nums)):
        #     if i%2 == 0:
        #         evens.append(nums[i])
        #     else:
        #         odds.append(nums[i])
        # evens.sort()
        # odds.sort()
        # odds=odds[::-1]
        # odd_idx , even_idx = 0 , 0

        # for i in range(len(nums)):

        #     if i %2 ==0:
        #         answer.insert(i,evens[even_idx])
        #         even_idx +=1
        #     else:
        #         answer.insert(i,odds[odd_idx])
        #         odd_idx +=1
        # return answer

        #Approach 02
        return reduce(add, zip_longest(sorted(nums[::2]), sorted(nums[1::2], reverse=True)))[:-1 if len(nums) % 2 else None]
        #Explain:
        # evens = sorted(nums[::2])
        # odds = sorted(nums[1::2], reverse=True)
        # #                       \U0001f813 Made flat zip(), see stackoverflow.com/questions/61943924/python-flat-zip
        # total = [num for num in chain.from_iterable(itertools.zip_longest(evens, odds)) if num is not None]
        # 
