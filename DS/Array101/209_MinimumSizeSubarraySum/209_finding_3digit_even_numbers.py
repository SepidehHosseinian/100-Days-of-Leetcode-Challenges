from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        #approach 01
        return sorted(list({ i*100+j*10+p for i,j,p in permutations(digits,3)if i!=0 and p%2==0}))
        
        #approach 02
        # res, cnt = [], Counter(digits)
        # for i in range(1, 10):
        #     for j in range(0, 10):
        #         for k in range(0, 10, 2):
        #             if cnt[i] > 0 and cnt[j] > (i == j) and cnt[k] > (k == i) + (k == j):
        #                 res.append(i * 100 + j * 10 + k)
        # return res

        #approach 03
        # hmap, res = defaultdict(int), []
        # for num in digits:
        #     hmap[num] += 1   #counting frequency of digits of digits array
        
        # for num in range(100, 999, 2):  #step 2 because we need even numbers
        #     checker = defaultdict(int)
        #     for digit in str(num):
        #         checker[int(digit)] += 1    #counting frequency of digits of num
            
		# 	#check if every digit in num is in digits array and its frequency is less than or equal to its frequency in digits array
        #     if all(map(lambda x: x in hmap and checker[x] <= hmap[x], checker)):
        #         res.append(num)
        
        # return res
