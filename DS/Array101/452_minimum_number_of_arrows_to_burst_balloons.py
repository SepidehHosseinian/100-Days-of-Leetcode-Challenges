class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])      # Example:  points = [[2,4],[1,6],[1,3],[7,8]]
                                               #      points.sort = [[1,3],[2,4],[1,6],[7,8]]
        tally, bow = 1, points[0][1]
                                               #                     ––––––– [7,9]
        for start, end in points:              #   ––––––––––––––––          [1,6] 
            if bow < start:                    #      –––––––                [2,4]
                bow = end                      #   –––––––                   [1,3]
                tally += 1                     #   1  2  3  4  5  6  7  8  9
                                               #         |                 |     
        return tally                           #     tally = 1         tally = 2
