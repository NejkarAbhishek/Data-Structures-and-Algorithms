class Solution(object):
    def helper(self, i, subsets, curSet, nums):
        if i >= len(nums):
            subsets.append(list(curSet))
            return
        curSet.append(nums[i])
        self.helper(i + 1, subsets, curSet, nums)
        curSet.pop()
        self.helper(i + 1, subsets, curSet, nums)

    def subsets(self, nums):
        subsets, curSet = [], []
        self.helper(0, subsets, curSet, nums)
        return subsets

    