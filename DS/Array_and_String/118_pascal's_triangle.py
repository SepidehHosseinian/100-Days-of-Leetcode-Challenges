class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res=[]
        intermedate=[]
        res.append([1])
        for i in range (numRows-1):
            intermedate=[1]
            for j in range (i):
              intermedate.append(res[i][j]+res[i][j+1])
            intermedate.append(1)
            res.append(intermedate)
        return res
        #118