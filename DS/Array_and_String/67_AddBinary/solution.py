class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a=int(a, 2)
        num_b=int(b, 2)
        res=bin(num_a+num_b)
        return res[2:]
        #67
