from ast import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for asteroid in asteroids:
            if not stk or asteroid > 0:
                stk.append(asteroid)
            else:
                while stk and stk[-1] > 0 and stk[-1] < abs(asteroid):
                    stk.pop()

                if stk and stk[-1] == abs(asteroid):
                    stk.pop()
                else:
                    if not stk or stk[-1] < 0:
                        stk.append(asteroid)
        
        return stk
       