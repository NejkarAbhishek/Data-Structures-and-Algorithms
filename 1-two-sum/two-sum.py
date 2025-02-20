class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        map = {}

        for index,value in enumerate(nums):
            diff=target-value
            if diff in map:
                return [map[diff],index]
            map[value]=index
        
        
            