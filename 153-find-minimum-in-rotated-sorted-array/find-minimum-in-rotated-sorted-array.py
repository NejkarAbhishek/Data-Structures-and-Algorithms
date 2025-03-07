class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        s,e=0,len(nums)-1
        while s<=e:
            if nums[s] < nums [e]:
                res = min(res,nums[s])
                break
            
            m=(s+e)//2
            res = min(res,nums[m])
            if nums[m] >= nums[s]:
                s = m + 1
            else:
                e= m -1

        return res