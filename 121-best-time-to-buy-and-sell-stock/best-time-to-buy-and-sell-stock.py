class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L=0
        maxProfit=0
        for R in range(L+1,len(prices)):
            if prices[R]<prices[L]:
                L=R
            profit=prices[R]-prices[L]
            maxProfit=max(maxProfit,profit)

        return maxProfit
            
