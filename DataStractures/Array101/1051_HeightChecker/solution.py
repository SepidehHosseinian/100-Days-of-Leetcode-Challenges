class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        
        initial_heights =heights.copy()
        
        for i in range(len(heights)):
            min_index=i
            
            for j in range(i+1, len(heights)):
                
                if heights[j]<heights[i]:
                    heights[min_index], heights[j]=heights[j], heights[min_index]
                    
        
                
        
        
        counter =0
        for i in range(len(heights)):
            
            if heights[i] != initial_heights[i]:
                counter +=1
                
        return counter