class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        l,r=0,len(height)-1

        while l<r:
            area=min(height[l],height[r])*(r-l)
            maxArea=max(maxArea,area)
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return maxArea