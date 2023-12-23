class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n==1:
                return True
            elif n in visited:
                return False
            else:
                visited.add(n)
                n = sum(int(i)**2 for i in str(n))
    #202