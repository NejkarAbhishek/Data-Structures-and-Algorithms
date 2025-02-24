class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        area=0
        while l < r:
            maxArea=min(height[l],height[r])*(r-l)
            if height[l] < height[r]:
                l+=1
            elif height[r] < height[l]:
                r-=1
            else:
                l+=1

            area=max(maxArea,area)
        
        return area