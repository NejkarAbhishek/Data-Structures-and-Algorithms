import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        L,R=1,max(piles)
        res=R
       
        while L<=R:
            mid=(L+R)//2
            hrs=0
            for pile in piles:
                hrs += math.ceil(pile / float(mid))
            if hrs<=h:
                res=mid
                R=mid-1
            else:
                L=mid+1
  
        return res
