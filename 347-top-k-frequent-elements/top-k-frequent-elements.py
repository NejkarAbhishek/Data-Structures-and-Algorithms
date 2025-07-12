class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map ={}

        for num in nums:
            map[num] = 1 + map.get(num,0)
        
        res=[]

        while k:
            max_value=max(map,key=map.get)
            map.pop(max_value)
            res.append(max_value)
            k-=1
        
        return res