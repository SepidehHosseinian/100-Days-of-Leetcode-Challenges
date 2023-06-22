class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # ans=[]
        # temp = []
        # temp_2 = []

        # for n in nums1:
        #     if n not in nums2 and n not in temp:
                
        #         temp.append(n)
                
        # for m in nums2:   
        #     if m not in nums1 and m not in temp_2 :
        #         temp_2.append(m)
        # ans.append(temp)
        # ans.append(temp_2)
        # return ans
        #approach 02
        return [set(nums1)-set(nums2),set(nums2)-set(nums1)]
