class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        #Approach 01
        ans =[]
        if firstList is None or secondList is None:
            return ans
        else:
            for i in range(len(firstList)):
                for j in range(len(secondList)):
                    max_start = max(firstList[i][0], secondList[j][0])
                    min_finish = min(firstList[i][1], secondList[j][1])
                    if max_start>min_finish:
                        continue
                    else:
                        ans.append([max_start, min_finish])
        return ans


        #Approach 02
        # index1 = index2 = 0
        # start, end = 0, 1
        # merged_list = []
        # while index1 < len(firstList) and index2 < len(secondList):
        #     overlap1 = firstList[index1][start] <= secondList[index2][end] \
        #     and firstList[index1][start] >= secondList[index2][start]
            
        #     overlap2 = secondList[index2][start] <= firstList[index1][end] \
        #     and secondList[index2][start] >= firstList[index1][start]
            
        #     if overlap1 or overlap2:
        #         merged_list.append([max(firstList[index1][start], secondList[index2][start]), min(firstList[index1][end], secondList[index2][end])])
        #     if firstList[index1][end] < secondList[index2][end]:
        #         index1 += 1
        #     else:
        #         index2 += 1
        # return merged_list
