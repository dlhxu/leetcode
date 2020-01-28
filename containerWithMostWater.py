class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        right = len(height) - 1
        left = 0
        maxArea = -1
        
        while(right > left):
            limitingHeight = min(height[right], height[left])
            area = limitingHeight * (right-left)
            if(area > maxArea):
                maxArea = area
            
            if (limitingHeight == height[right]):
                right -=1
            else:
                left +=1
        
        return maxArea
