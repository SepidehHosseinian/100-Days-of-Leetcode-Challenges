class Solution:
    def largestInteger(self, num: int) -> int:
        n = len(str(num))
        digit_list = [int(i) for i in str(num)]
 
        odds=[]
        evens=[]
        
        for i in digit_list:
            if i%2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        
        odds.sort()
        evens.sort()

        ans = [odds.pop() if digit_list[d]%2 else evens.pop() for d in range(n)]
        return (sum([d*10**(len(ans)-i-1) for i,d in enumerate(ans)]))
