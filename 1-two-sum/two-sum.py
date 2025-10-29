class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map={}

        for index, value in enumerate(nums):
            if target-nums[index] in map:
                return [map[target-nums[index]],index]
            map[value]=index
        return [-1,-1]
