from ast import List


class Solution:
    def PredictTheWinner(self, A: List[int]) -> bool:
        memo = {}
        def maxscore(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i>j:
                return 0
            #
            sA = A[i] + min( maxscore(i+1,j-1), maxscore(i+2,j  ) ) # pick A[i] + min of the 2 possible upcoming turns (player 2 is smart)
            sB = A[j] + min( maxscore(i  ,j-2), maxscore(i+1,j-1) )
            score = max(sA,sB)
            memo[i,j] = score
            return score
        p1 = maxscore(0,len(A)-1) # Score Player 1
        return p1>=(sum(A)-p1) # p1 >= p2