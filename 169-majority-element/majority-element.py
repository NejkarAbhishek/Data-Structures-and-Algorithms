class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,count=0,0
        for i in range(len(nums)):
            if nums[i] == res:
                count += 1
            elif count == 0:  
                res = nums[i]
                count = 1
            else:
                count -= 1 

        return res
