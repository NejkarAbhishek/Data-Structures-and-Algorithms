class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        L,R=0,len(height)-1
        while L < R:
            area =min(height[L], height[R]) * (R-L)
            maxArea=max(maxArea,area)
            if height[L] < height[R]:
                L+=1
            elif height[R] < height[L]:
                R-=1
            else:
                R-=1
        
        return maxArea